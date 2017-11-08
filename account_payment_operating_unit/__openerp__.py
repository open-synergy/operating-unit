# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Account Payment Operating Unit",
    "version": "8.0.0.0.0",
    "license": 'AGPL-3',
    "author": "OpenSynergy Indonesia, "
              "Odoo Community Association (OCA)",
    "website": "https://opensynergy-indonesia.com",
    "category": "Accounting",
    "depends": [
        "account_operating_unit",
        "account_payment",
    ],
    "data": [
        "views/payment_order_views.xml",
        "security/account_payment_security.xml"
    ],
    'installable': True,
}
