{
    'name': 'Peluquería IZL',
    'version': '1.0',
    'author': 'Ian Zapatero López',
    'category': 'Servicios',
    'summary': 'Gestión de clientes, citas, empleados y servicios de la peluquería',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'security/izl_peluqueria_groups.xml',
        'data/sequence.xml',
        'views/cliente_views.xml',
        'views/empleado_views.xml',
        'views/servicio_views.xml',
        'views/cita_views.xml',
        'views/cita_search_views.xml',
        'views/izl_peluqueria_menus.xml',
        'views/cliente_search_views.xml',
        'views/empleado_search_views.xml',
        'views/cliente_kanban_views.xml',
        'data/izl_peluqueria_demo.xml'
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True
}
