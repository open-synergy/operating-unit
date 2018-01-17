# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Operating Unit in Account Voucher Bank and Cash",
    "version": "8.0.1.0.0",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "website": "https://opensynergy-indonesia.com",
    "category": "Accounting",
    "depends": [
        "account_voucher_bank_cash",
        "account_voucher_common_operating_unit"
    ],
    "data": [
        "security/account_bank_receipt_security.xml",
        "security/account_bank_payment_security.xml",
        "security/account_cash_receipt_security.xml",
        "security/account_cash_payment_security.xml"
    ],
    "installable": True,
    "auto_install": True,
}
