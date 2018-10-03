{
    'name': 'Rastreadores UTM',
    'description': """
Ativar rastreadores UTM em links compartilhados.
=====================================================
        """,
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/utm.xml',
        'data/utm_data.xml'
    ],
}
