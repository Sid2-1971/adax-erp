# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Produtos',
    'version': '1.2',
    'depends': ['base', 'decimal_precision', 'mail'],
    'data': [
        'data/product_data.xml',
        'security/product_security.xml',
        'security/ir.model.access.csv',
        'wizard/product_price_list_views.xml',
        'views/res_config_settings_views.xml',
        'views/product_attribute_views.xml',
        'views/product_uom_views.xml',
        'views/product_views.xml',
        'views/product_template_views.xml',
        'views/product_pricelist_views.xml',
        'views/res_partner_views.xml',
        'report/product_reports.xml',
        'report/product_pricelist_templates.xml',
        'report/product_product_templates.xml',
        'report/product_template_templates.xml',
    ],
    'installable': True,
    'auto_install': False,
}
