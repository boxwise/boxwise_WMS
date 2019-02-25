# -*- coding: utf-8 -*-
{
    'name': "Boxwise Warehouse Management",

    'summary': "WMS for inkind-donations",

    'author': "Humanilog",
    'website': "www.humanilog.org",

    'category': 'Uncategorized',
    'version': '11.0.1.0.5',

    'depends': ['stock', 'website_menu_by_user_status', 'boxwise_wms_pampiraiki'],
    'post_init_hook': 'post_init_hook',

    'data': [
        'data/main_partner.xml',
        'data/website_menu.xml',
        'data/website_page.xml',
        'data/website_settings.xml',
        'data/inventory_settings.xml',
        'data/user_groups.xml',
        'views/packages.xml',
        'views/home.xml',
        'views/box_edit.xml',
        'views/box_view.xml',
        'templates/layout.xml',
        'templates/assets.xml',

        'views/generate_qr.xml',
        'data/report.paperformat.csv',
        'reports/report_qr_codes.xml',
        'reports/report_qr_codes_alt.xml',
        'reports/report_qr_codes_alt2.xml',

        # leave at bottom
        'data/init.xml',
    ],
}
