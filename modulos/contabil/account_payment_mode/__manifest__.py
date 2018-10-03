# -*- coding: utf-8 -*-
# © 2016 Akretion (<https://www.akretion.com>).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Account Payment Mode',
    'version': '1.1',
    'category': 'Banking addons',
    'depends': ['account'],
    'data': [
        'security/account_payment_mode.xml',
        'security/ir.model.access.csv',
        'views/account_payment_method.xml',
        'views/account_payment_mode.xml',
        'views/res_partner_bank.xml',
        'views/res_partner.xml',
        'views/account_journal.xml',
    ],
    'installable': True,
}
