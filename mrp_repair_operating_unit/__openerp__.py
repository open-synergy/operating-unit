# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Repair Order Operating Unit",
    "version": "8.0.0.0.0",
    "license": 'AGPL-3',
    "author": "OpenSynergy Indonesia, "
              "Odoo Community Association (OCA)",
    "website": "https://opensynergy-indonesia.com",
    "category": "Manufacturing",
    "depends": [
        "mrp_repair",
        "stock_operating_unit",
    ],
    "data": [
        "views/mrp_repair_views.xml",
        "security/mrp_repair_security.xml"
    ],
    'installable': True,
}
