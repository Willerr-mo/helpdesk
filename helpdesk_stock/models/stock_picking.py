# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import models, fields


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    ticket_id = fields.Many2one(
        comodel_name="helpdesk.ticket",
        string="Helpdesk Ticket")
