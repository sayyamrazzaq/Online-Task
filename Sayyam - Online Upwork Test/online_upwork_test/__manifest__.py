# -*- coding: utf-8 -*-
{
    'name': "Online Upwork Test",

    'summary': """
    Translate operation tyYpe name""",

    'description': """
        Translate operation tyYpe name
    """,

    'author': "Sayyam Abdul Razzaq",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'stock',
    'version': '13.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
}
