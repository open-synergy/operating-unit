# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import fields, models


class SaleOrderBlanketLine(models.Model):
    _inherit = "sale.order.blanket.line"

    operating_unit_id = fields.Many2one(
        string="Default Operating Unit",
        comodel_name="operating.unit",
        related="order_id.operating_unit_id",
        readonly=True,
    )
