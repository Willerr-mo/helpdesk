# Copyright 2018 Angel Moya
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class HelpdeskTicketAction(models.Model):
    _name = 'helpdesk.ticket.action'
    _description = 'Helpdesk Stage'

    name = fields.Char(string='Action')
    ticket_id = fields.Many2one(
        string='Ticket',
        comodel_name='helpdesk.ticket')
