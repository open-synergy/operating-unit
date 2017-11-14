# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from openerp import fields, models


class AccountAnalyticPlanInstance(models.Model):

    _inherit = "account.analytic.plan.instance"

    operating_unit_ids = fields.Many2many(
        comodel_name="operating.unit", string="Operating Units",
        relation="analytic_plan_instance_operating_unit_rel",
        column1="analytic_plan_instance_id",
        column2="operating_unit_id")
