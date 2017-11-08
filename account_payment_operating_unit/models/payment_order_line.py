# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from openerp import fields, models


class PaymentOrderLine(models.Model):

    _inherit = "payment.line"

    operating_unit_id = fields.Many2one(
        comodel_name="operating.unit",
        string="Source Location Operating Unit",
        related="order_id.operating_unit_id",
        readonly=True,
    )
