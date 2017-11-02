# -*- coding: utf-8 -*-
# Copyright 2014 Eficent Business and IT Consulting Services S.L. -
# Jordi Ballester Alomar
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


{
    "name": "HR Expense Operating Unit",
    "version": "8.0.1.0.0",
    "license": 'AGPL-3',
    "author": "Eficent Business and IT Consulting Services S.L., "
              "Odoo Community Association (OCA)",
    "category": "Generic Modules/Human Resources",
    "depends": ["hr_expense", "account_operating_unit"],
    "data": [
        "views/hr_expense_view.xml",
        "security/hr_expense_security.xml"
    ],
    'demo': [],
    'installable': True,
}
