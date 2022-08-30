{
    'name': 'Partner SR Team Code',
    'version': '15.0.0.0',
    'summary': 'Partner SR Team Code',
    'description': 'Add Partner SR Team Code, and make it available to search with',
    'category': '',
    'author': '',
    'website': '',
    'license': '',
    'depends': ['base','sale'],
    'data': [
        'security/ir.model.access.csv',
        
        'views/city_team.xml',
        'views/sale_order.xml',
        
    ],
    'installable': True,
    'auto_install': False,
}