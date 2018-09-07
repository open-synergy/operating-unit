# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "PoS Order Summary with Operating Units",
    "version": "8.0.1.0.0",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "website": "https://opensynergy-indonesia.com",
    "category": "Point Of Sale Management",
    "depends": [
        "pos_order_summary",
        "pos_operating_unit"
    ],
    "data": [
        "security/pos_order_summary_security.xml",
        "views/pos_order_summary_by_product.xml",
        "views/pos_order_summary_by_transaction.xml"
    ],
    'installable': True,
}
