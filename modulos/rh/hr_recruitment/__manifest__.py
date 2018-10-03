# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'RH - Recrutamento',
    'version': '1.0',
    'sequence': 90,

    'depends': [
        'hr',
        'calendar',
        'fetchmail',
        'utm',
        'document',
    ],
    'data': [
        'security/hr_recruitment_security.xml',
        'security/ir.model.access.csv',
        'data/hr_recruitment_data.xml',
        'views/hr_recruitment_views.xml',
        'views/res_config_settings_views.xml',
        'views/hr_recruitment_templates.xml',
        'views/hr_department_views.xml',
        'views/hr_job_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
