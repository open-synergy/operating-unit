# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author

{
    "name": "Operating Unit in Account Voucher",
    "version": "8.0.1.1.0",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "website": "https://opensynergy-indonesia.com",
    "category": "Accounting",
    "depends": [
        "account_voucher_common",
        "account_operating_unit"
    ],
    "data": [
        "views/account_voucher_common_views.xml"
    ],
    'installable': True,
}
