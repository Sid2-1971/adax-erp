#-*- coding:utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Conexão SMTP/POP',
    'version': '1.0',
    'depends': ['mail'],
    'data': [
        'data/fetchmail_data.xml',
        'security/ir.model.access.csv',
        'views/fetchmail_views.xml',
        'views/mail_mail_views.xml',
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'auto_install': True,
}
