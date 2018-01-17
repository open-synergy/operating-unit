# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Operating Unit in Account Voucher Cheque",
    "version": "8.0.1.0.0",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "website": "https://opensynergy-indonesia.com",
    "category": "Accounting",
    "depends": [
        "account_voucher_cheque",
        "account_voucher_common_operating_unit"
    ],
    "data": [
        "security/account_cheque_receipt_security.xml",
        "security/account_cheque_payment_security.xml"
    ],
    "installable": True,
    "auto_install": True,
}
