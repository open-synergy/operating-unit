# -*- coding: utf-8 -*-
# Copyright 2016Noviat nv/sa (www.noviat.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Operating Unit on Bank Statement',
    'version': '8.0.0.0.0',
    'license': 'AGPL-3',
    "author": "Noviat, "
              "Odoo Community Association (OCA)",
    'category': 'Accounting & Finance',
    'summary': 'Encode Bank Statements with Operating Units',
    'depends': ['account_operating_unit'],
    'data': [
        'security/account_security.xml',
        'views/account_bank_statement.xml',
        'views/assets_backend.xml',
    ],
    'installable': True,
}
