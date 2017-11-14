# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Analytic Plan Operating Unit",
    "version": "8.0.0.0.0",
    "author": "OpenSynergy Indonesia, "
              "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "website": "https://opensynergy-indonesia.com",
    "category": "Sales",
    "depends": [
        "analytic_operating_unit",
        "account_analytic_plans"],
    "data": [
        "security/analytic_plan_security.xml",
        "views/account_analytic_plan_views.xml",
        "views/account_analytic_plan_instance_views.xml",
    ],
    'installable': True,
}
