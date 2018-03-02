# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models


class ChequePayment(models.Model):
    _name = "account.cheque_payment"
    _inherit = [
        "account.cheque_payment",
        "account.voucher_common"
    ]
