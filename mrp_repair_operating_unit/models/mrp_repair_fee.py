# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from openerp import fields, models


class MrpRepairFee(models.Model):

    _inherit = "mrp.repair.fee"

    operating_unit_id = fields.Many2one(
        comodel_name="operating.unit",
        string="Operating Unit",
        related="repair_id.operating_unit_id",
        readonly=True,
        store=True
    )
