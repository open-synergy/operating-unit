# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models


class PurchaseAdvanceSettlement(models.Model):
    _name = "account.purchase_advance_settlement"
    _inherit = [
        "account.purchase_advance_settlement",
        "account.voucher_common"
    ]
