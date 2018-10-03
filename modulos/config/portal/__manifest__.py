# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Customer Portal',
    'sequence': '9000',
    'category': 'Hidden',
    'depends': ['http_routing', 'mail'],
    'data': [
        'data/portal_data.xml',
        'views/assets.xml',
        'views/portal_templates.xml',
        'wizard/portal_wizard_views.xml',
    ],
    'qweb': [
        'static/src/xml/portal_chatter.xml',
        'static/src/xml/portal_signature.xml',
    ],
}
