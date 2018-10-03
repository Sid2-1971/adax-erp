# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Gestão de Vendas',
    'version': '1.0',
    'sequence': 15,
    'depends': ['sale', 'account_invoicing'],
    'data': [
        'views/sale_management_views.xml',
        'views/sale_management_templates.xml',
    ],
    'application': True,
    'uninstall_hook': 'uninstall_hook',
    'post_init_hook': 'post_init_hook',
}
