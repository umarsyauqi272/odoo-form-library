# -*- coding: utf-8 -*-
{
    'name': "Library Management",

    'summary': """
        Memudahkan pustakawan dalam mengelola perpustakaan, mulai dari buku, siswa serta peminjaman""",

    'description': """
        Memudahkan pustakawan dalam mengelola perpustakaan, mulai dari buku, siswa serta peminjaman
    """,
    'installable': True,
    'application': True,
    'author': "Umar Syauqi Abdullah",
    'website': "https://abdullahumar.utschool.id/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
