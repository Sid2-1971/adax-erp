# -*- coding: utf-8 -*-

{
    'name': 'Oportunidade em contação',
    'version': '1.0',
    'description': """
Este módulo adiciona um atalho em um ou vários casos de oportunidade no CRM.
===========================================================================

Esse atalho permite gerar um pedido de vendas com base no caso selecionado. 
Se diferentes casos estiverem abertos (uma lista), ele gera uma ordem de 
vendas por caso. O caso é então fechado e vinculado ao pedido de venda gerado.

Sugerimos que você instale este módulo, se você instalou os módulos de venda e de CRM.
    """,
    'depends': ['sale_management', 'crm'],
    'data': [
        'security/ir.model.access.csv',
        'views/partner_views.xml',
        'views/sale_order_views.xml',
        'views/crm_lead_views.xml',
    ],
    'auto_install': True,
}
