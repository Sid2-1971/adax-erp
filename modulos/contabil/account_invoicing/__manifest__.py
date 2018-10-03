# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Faturamento',
    'version': '1.0',
    'sequence': 30,
    'depends': ['account'],
    'data': [
        'views/account_menuitem_views.xml',
        'views/product_template_views.xml',
        'views/account_invoicing_templates.xml',
        'views/account_invoicing_views.xml',

    ],
    'qweb': [
    ],
    'application': True,
    'uninstall_hook': 'uninstall_hook',
    'post_init_hook': 'post_init_hook',
}
