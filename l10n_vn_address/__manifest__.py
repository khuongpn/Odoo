# -*- coding: utf-8 -*-
# Copyright (C): khuongphampn@gmail.com

{
    'name': 'VN Address',
    'version': '11.0',
    'category': 'Base',
    'sequence': 1,
    'author': 'khuongphampn@gmail.com',
    'summary': 'Address VN',
    'description': """
VN Address
==========================


You can manage:
---------------
    * Address VN
    """,
    'website': 'https://www.dodo-odoo.com',
    'images': [

    ],
    'depends': [
        'contacts',
    ],
    'data': [
        # data
        'data/res_country_level_data.xml',
        'data/res.country.state.csv',
        'data/res.country.district.csv',
        'data/res.country.ward.csv',
        'data/res_country_data.xml',

        # views
        'views/res_country_ward_view.xml',
        'views/res_country_district_view.xml',
        'views/res_country_state_view.xml',
        'views/res_country_level_view.xml',
        'views/res_partner_views.xml',

        #menu
        'menu/address_menu.xml',
        
        #security
        'security/ir.model.access.csv',
    ],
    'demo': [

    ],
    'test': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
}
