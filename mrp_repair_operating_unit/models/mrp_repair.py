# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from openerp import fields, models


class MrpRepair(models.Model):

    _inherit = "mrp.repair"

    operating_unit_id = fields.Many2one(
        comodel_name="operating.unit",
        string="Operating Unit",
        default=lambda self:
        self.env['res.users'].
        operating_unit_default_get(self._uid),
    )
