# -*- coding: utf-8 -*-
# © 2016 Eficent Business and IT Consulting Services S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Analytic Operating Unit",
    "version": "8.0.1.0.0",
    "author": "Eficent, "
              "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "website": "https://github.com/OCA/operating-unit",
    "category": "Sales",
    "depends": ["analytic", "operating_unit"],
    "data": [
        "views/analytic_account_view.xml",
        "security/analytic_account_security.xml",
    ],
    'installable': True,
}
