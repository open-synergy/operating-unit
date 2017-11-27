# -*- coding: utf-8 -*-
# © 2017 Genweb2 Limited - Matiar Rahman
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from openerp import api, fields, models


class HREmployee(models.Model):
    _inherit = 'hr.employee'

    @api.model
    def operating_unit_default_get(self, uid2):
        if not uid2:
            uid2 = self._uid
        user = self.env['res.users'].browse(uid2)
        return user.default_operating_unit_id

    @api.model
    def _get_operating_unit(self):
        return self.operating_unit_default_get(self._uid)

    @api.model
    def _get_operating_units(self):
        return self._get_operating_unit()

    operating_unit_ids = fields.Many2many('operating.unit',
                                          'operating_unit_emp_rel',
                                          'emp_id', 'ou_id', 'Operating Units',
                                          default=_get_operating_units)
