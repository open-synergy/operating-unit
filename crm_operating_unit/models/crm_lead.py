# -*- coding: utf-8 -*-
# © 2015 Eficent Business and IT Consulting Services S.L. -
# Jordi Ballester Alomar
# © 2015 Serpent Consulting Services Pvt. Ltd. - Sudhir Arya
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from openerp import api, fields, models
from openerp.exceptions import Warning
from openerp.tools.translate import _


class CRMLead(models.Model):

    _inherit = 'crm.lead'

    operating_unit_id = fields.Many2one('operating.unit', 'Operating Unit',
                                        default=lambda self:
                                        self.env['res.users'].
                                        operating_unit_default_get(self._uid))

    @api.one
    @api.constrains('operating_unit_id', 'company_id')
    def _check_company_operating_unit(self):
        if self.company_id and \
                self.operating_unit_id and \
                self.company_id != self.operating_unit_id.company_id:
            raise Warning(_('Configuration error!\nThe Company in the\
        CRM Lead and in the Operating Unit must be the same.'))
