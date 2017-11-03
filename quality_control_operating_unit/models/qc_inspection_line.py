# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from openerp import fields, models


class QcInspectionLine(models.Model):

    _inherit = "qc.inspection.line"

    operating_unit_id = fields.Many2one(
        comodel_name="operating.unit",
        string="Operating Unit",
        related="inspection_id.operating_unit_id",
        readonly=True,
        store=True
    )
