# -*- coding: utf-8 -*-
# © 2014 Akretion - Alexis de Lattre <alexis.delattre@akretion.com>
# © 2014 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Account Payment Partner',
    'version': '2.1',
    'depends': ['account_payment_mode'],
    'data': [
        'views/res_partner_view.xml',
        'views/account_invoice_view.xml',
        'views/account_move_line.xml',
        'views/report_invoice.xml',
    ],
    'installable': True,
}
