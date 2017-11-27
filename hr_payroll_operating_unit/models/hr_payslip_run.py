# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import fields, models


class HrPayslipRun(models.Model):
    _inherit = "hr.payslip.run"

    operating_unit_id = fields.Many2one(
        string="Default Operating Unit",
        comodel_name="operating.unit",
        default=lambda self:
        self.env['res.users'].
        operating_unit_default_get(self._uid)
    )
