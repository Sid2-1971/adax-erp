{
    'name': 'Contratos - Recorrentes',
    'version': '2.1',
    'depends': ['base', 'account', 'analytic'],
    'data': [
        'security/ir.model.access.csv',
        'security/contract_security.xml',
        'report/report_contract.xml',
        'report/contract_views.xml',
        'data/contract_cron.xml',
        'data/mail_template.xml',
        'views/account_analytic_account_view.xml',
        'views/account_analytic_contract_view.xml',
        'views/account_invoice_view.xml',
        'views/res_partner_view.xml',
    ],
    'installable': True,
}
