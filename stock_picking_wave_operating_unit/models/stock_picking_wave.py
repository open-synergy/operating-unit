# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models, api


class StockPickingWave(models.Model):
    _inherit = "stock.picking.wave"

    operating_unit_id = fields.Many2one(
        string="Default Operating Unit",
        comodel_name="operating.unit"
    )

    @api.onchange(
        "type_id")
    def onchange_ou_id(self):
        wave_type = self.type_id
        warehouse_id = wave_type.warehouse_id
        ou_user =\
            self.env['res.users'].operating_unit_default_get(self._uid)

        if warehouse_id:
            ou = wave_type.warehouse_id.operating_unit_id
            if not ou:
                self.operating_unit_id = ou_user.id
            else:
                self.operating_unit_id = ou.id
        else:
            self.operating_unit_id = ou_user.id
