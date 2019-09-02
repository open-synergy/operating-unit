# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import api, fields, models
from openerp.exceptions import Warning as UserError
from openerp.tools.translate import _


class SaleOrderBlanket(models.Model):
    _inherit = "sale.order.blanket"

    operating_unit_id = fields.Many2one(
        string="Default Operating Unit",
        comodel_name="operating.unit",
        default=lambda self:
        self.env["res.users"].
        operating_unit_default_get(self._uid)
    )

    @api.constrains(
        "operating_unit_id",
        "company_id"
    )
    def _check_company_operating_unit(self):
        strWarning = _(
            "Configuration error!\nThe Company in the "
            "Blanket Order and in the Operating Unit must be the same.")
        if self.company_id and\
                self.operating_unit_id and\
                self.company_id != self.operating_unit_id.company_id:
            raise UserError(strWarning)
