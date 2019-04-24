# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    project_id = fields.Many2one(
        comodel_name="project.project",
        string="Proyecto",
    )
    task_id = fields.Many2one(
        comodel_name="project.task",
        string="Tarea",
        required=True,
    )
    analytic_account_active = fields.Boolean(
        "Analytic Account",
        related='project_id.analytic_account_id.active',
        readonly=True
    )
    allow_timesheets = fields.Boolean(
        "Allow timesheets",
        related='project_id.allow_timesheets',
        help="Timesheets can be logged on this task.",
        readonly=True
    )
    subtask_count = fields.Integer(
        "Sub-task count",
        related='task_id.subtask_count',
        readonly=True
    )
    planned_hours = fields.Float(
        "Planned Hours",
        related='task_id.planned_hours',
        readonly=True
    )
    subtask_planned_hours = fields.Float(
        "Subtasks",
        related='task_id.subtask_planned_hours',
        readonly=True
    )
    progress = fields.Float(
        "Progress",
        related='task_id.progress',
        readonly=True
    )
    timesheet_ids = fields.One2many(
        related='task_id.timesheet_ids',
        string="Timesheets",
        readonly=False,
    )
    effective_hours = fields.Float(
        related='task_id.effective_hours',
        string="Hours Spent",
        readonly=True,
    )
    subtask_effective_hours = fields.Float(
        related='task_id.subtask_effective_hours',
        string="Sub-tasks Hours Spent",
        readonly=True,
    )
    total_hours_spent = fields.Float(
        related='task_id.total_hours_spent',
        string="Total Hours",
        readonly=True,
    )
    remaining_hours = fields.Float(
        related='task_id.remaining_hours',
        string="Remaining Hours",
        readonly=True,
    )

    @api.onchange('task_id')
    def _onchange_task_id(self):
        if self.task_id:
            self.project_id = self.task_id.project_id

    @api.onchange('project_id')
    def _onchange_project_id(self):
        self.partner_id = False
        res = {'domain': {'task_id': []}}
        if self.project_id:
            res['domain']['task_id'] = [
                ('project_id', '=', self.project_id.id)]
        return res
