# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    picking_ids = fields.One2many(
        comodel_name="stock.picking",
        inverse_name="ticket_id",
        string="Pickings")
