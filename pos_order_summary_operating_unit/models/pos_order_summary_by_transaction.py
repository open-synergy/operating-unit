# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class PosOrderSummaryByTransaction(models.AbstractModel):
    _inherit = "pos.order_summary_by_transaction"

    operating_unit_id = fields.Many2one(
        string="Default Operating Unit",
        comodel_name="operating.unit"
    )

    def _select(self):
        _super = super(PosOrderSummaryByTransaction, self)
        select_str = _super._select() + """
            ,D.operating_unit_id
        """
        return select_str
