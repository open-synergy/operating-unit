# -*- coding: utf-8 -*-
# Copyright 2016Noviat nv/sa (www.noviat.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class AccountBankStatementLine(models.Model):
    _inherit = 'account.bank.statement.line'

    operating_unit_id = fields.Many2one(
        comodel_name='operating.unit',
        string='Operating Unit',
        related='statement_id.operating_unit_id',
        readonly=True,
        store=True)

    @api.model
    def get_statement_line_for_reconciliation(self, st_line):
        data = super(AccountBankStatementLine, self).\
            get_statement_line_for_reconciliation(st_line)
        data['operating_unit_id'] = st_line.operating_unit_id.id
        return data
