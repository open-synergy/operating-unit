# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models


class GiroReceipt(models.Model):
    _name = "account.giro_receipt"
    _inherit = [
        "account.giro_receipt",
        "account.voucher_common"
    ]
