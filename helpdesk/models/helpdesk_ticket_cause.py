# Copyright 2018 Angel Moya
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class HelpdeskTicketCause(models.Model):
    _name = 'helpdesk.ticket.cause'
    _description = 'Helpdesk Stage'

    name = fields.Char(string='Cause')
