# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Blanket Order with Operating Units",
    "version": "8.0.1.0.0",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "website": "https://opensynergy-indonesia.com",
    "category": "Point Of Sale Management",
    "depends": [
        "sale_order_blanket",
        "operating_unit"
    ],
    "data": [
        "security/sale_order_blanket_security.xml",
        "views/sale_order_blanket_views.xml",
    ],
    "installable": True,
    "auto_install": True,
}
