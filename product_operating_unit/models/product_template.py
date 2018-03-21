# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    operating_unit_ids = fields.Many2many(
        string="Operating Units",
        comodel_name="operating.unit",
        relation="product_template_operating_unit_rel",
        column1="product_id",
        column2="operating_unit_id")
