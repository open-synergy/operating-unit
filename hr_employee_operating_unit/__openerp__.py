# -*- coding: utf-8 -*-
# © 2017 Genweb2 Limited - Matiar Rahman
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Employee Operating Unit",
    "version": "8.0.1.0.0",
    "author": "Matiar Rahman, "
              "Genweb2 Limited,"
              "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "website": "https://github.com/OCA/operating-unit",
    "category": "Human Resources",
    "depends": ["hr", "operating_unit"],
    "data": [
        "views/hr_views.xml",
        "security/security.xml",
    ],
    'installable': True,
    'application': False,
}
