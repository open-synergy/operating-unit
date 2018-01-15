# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import fields, models, api


class AccountVoucherCommon(models.Model):
    _inherit = "account.voucher_common"

    operating_unit_id = fields.Many2one(
        string="Default Operating Unit",
        comodel_name="operating.unit"
    )

    @api.onchange(
        "journal_id")
    def onchange_journal(self):
        res = super(AccountVoucherCommon, self).onchange_journal()

        journal = self.journal_id
        ou = journal.operating_unit_id

        if not ou:
            ou_user =\
                self.env['res.users'].operating_unit_default_get(self._uid)
            self.operating_unit_id = ou_user.id
        else:
            self.operating_unit_id = ou.id
        return res

    @api.multi
    def _prepare_account_move(self):
        res = super(AccountVoucherCommon, self)._prepare_account_move()
        res["operating_unit_id"] = self.operating_unit_id.id
        return res
