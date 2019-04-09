# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class StockReturnPicking(models.TransientModel):
    _inherit = 'stock.return.picking'

    ticket_id = fields.Many2one(
        comodel_name='helpdesk.ticket',
        string='Helpdesk Ticket')

    def create_returns(self):
        res = super(StockReturnPicking, self).create_returns()
        if self.ticket_id:
            self.env['stock.picking'].browse(res['res_id']).write(
                {'ticket_id': self.ticket_id.id}
            )
        return res
