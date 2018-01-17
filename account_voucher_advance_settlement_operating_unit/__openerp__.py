# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Operating Unit in Account Voucher Advance Settlement",
    "version": "8.0.1.0.0",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "website": "https://opensynergy-indonesia.com",
    "category": "Accounting",
    "depends": [
        "account_voucher_advance_settlement",
        "account_voucher_common_operating_unit"
    ],
    "data": [
        "security/account_purchase_advance_settlement_security.xml",
        "security/account_sale_advance_settlement_security.xml"
    ],
    "installable": True,
    "auto_install": True,
}
