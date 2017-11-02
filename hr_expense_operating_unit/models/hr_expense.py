# -*- coding: utf-8 -*-
# Copyright 2014 Eficent Business and IT Consulting Services S.L. -
# Jordi Ballester Alomar
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api


class HrExpenseExpense(models.Model):

    _inherit = 'hr.expense.expense'

    operating_unit_id = fields.Many2one(
        'operating.unit',
        string='Operating Unit',
        default=lambda self: self.env['res.users'].
        operating_unit_default_get(self._uid),
    )

    @api.model
    def account_move_get(self, expense_id):
        res = super(HrExpenseExpense, self).account_move_get(expense_id)
        expense = self.browse(expense_id)
        if expense.operating_unit_id:
            res['operating_unit_id'] = expense.operating_unit_id.id
        return res
