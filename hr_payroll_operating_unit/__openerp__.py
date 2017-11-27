# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Operating Unit in Payroll",
    "version": "8.0.1.0.0",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "website": "https://opensynergy-indonesia.com",
    "category": "Human Resource Management",
    "depends": [
        "hr_payroll",
        "operating_unit"
    ],
    "data": [
        "security/hr_payroll_security.xml",
        "views/hr_payslip_run_views.xml"
    ],
    'installable': True,
}
