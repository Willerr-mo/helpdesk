# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "HelpDesk Stock",
    "summary":
        "Module to Support Teams",
    "version": "12.0.1.0.0",
    "category": "Customer Relationship Management",
    "website": "",
    "author": "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "data": [
        "views/helpdesk_ticket_views.xml",
        "views/stock_picking_inherit.xml",
        "views/stock_return_picking_inherit.xml",
    ],
    "installable": True,
    'auto_install': True,
    "depends": ["base", "stock", "helpdesk"],
}
