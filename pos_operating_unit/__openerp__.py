# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Operating Unit in POS",
    "version": "8.0.1.0.0",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "website": "https://opensynergy-indonesia.com",
    "category": "Point Of Sale Management",
    "depends": [
        "point_of_sale",
        "stock_operating_unit"
    ],
    "data": [
        "security/pos_security.xml",
        "views/pos_config_views.xml"
    ],
    'installable': True,
}
