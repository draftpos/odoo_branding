# -*- coding: utf-8 -*-
{
    'name': 'Odoo Branding & Navbar Customizer',
    'version': '19.0.1.0.0',
    'category': 'Extra Tools/Customization',
    'summary': 'Custom Company Logo on Top Navigation Bar & Dynamic Navbar Theming',
    'description': """
Odoo Branding & Navbar Customizer
=================================
A modern, multi-company branding extension for Odoo:
- Positions company logo on top-left navigation bar before app menu icons
- Full UI color pickers for background, text, active highlights, and hover states
- Crisp high-contrast rendering across both dark and light modes
- Multi-company aware with instant live theming
    """,
    'author': 'Havano / Tatenda Tembo',
    'website': 'https://havano.pro',
    'license': 'LGPL-3',
    'depends': ['base', 'web', 'base_setup'],
    'data': [
        'views/res_config_settings_views.xml',
        'views/res_company_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'odoo_branding/static/src/scss/navbar_branding.scss',
            'odoo_branding/static/src/webclient/navbar/navbar_branding.xml',
            'odoo_branding/static/src/webclient/navbar/navbar_branding.js',
        ],
    },
    'images': [
        'static/description/icon.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
