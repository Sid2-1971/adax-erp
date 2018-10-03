# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Painel de Configurações',
    'version': '1.0',
    'data': [
        'views/dashboard_views.xml',
        'views/dashboard_templates.xml',
    ],
    'depends': ['web_planner'],
    'qweb': ['static/src/xml/dashboard.xml'],
    'auto_install': True,
}
