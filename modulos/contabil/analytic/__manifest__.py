# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Analytic Accounting',
    'version': '1.1',
    'depends' : ['base', 'decimal_precision', 'mail'],
    'data': [
        'security/analytic_security.xml',
        'security/ir.model.access.csv',
        'views/analytic_account_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}
