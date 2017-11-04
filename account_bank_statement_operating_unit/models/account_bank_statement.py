# -*- coding: utf-8 -*-
# Copyright 2016Noviat nv/sa (www.noviat.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class AccountBankStatement(models.Model):
    _inherit = 'account.bank.statement'

    operating_unit_id = fields.Many2one(
        comodel_name='operating.unit',
        string='Operating Unit')

    @api.multi
    def onchange_journal_id(self, journal_id):
        res = super(AccountBankStatement, self).onchange_journal_id(journal_id)
        journal = self.env['account.journal'].browse(journal_id)
        ou = journal.default_debit_account_id.operating_unit_id
        if not ou:
            ou = self.env['res.users'].operating_unit_default_get(self._uid)
        ou_id = ou and ou.id
        if not res:
            res = {'value': {'operating_unit_id': ou_id}}
        else:
            res['value']['operating_unit_id'] = ou_id
        return res
