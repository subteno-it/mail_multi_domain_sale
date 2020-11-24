# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

{
    'name': "mail_multi_domain_sale",
    'summary': "Force alias domain by Sales Team",
    'description': """
        Long description of module's purpose
    """,
    'author': "Subteno IT",
    'website': "https://www.subteno-it.com",
    'category': 'Discuss',
    'version': '0.1',
    'depends': [
        'mail_multi_domain',
        'sale',
    ],
    'data': [
        'views/crm_team.xml',
    ],
}