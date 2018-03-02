# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models


class BankReceipt(models.Model):
    _name = "account.bank_receipt"
    _inherit = [
        "account.bank_receipt",
        "account.voucher_common"
    ]
