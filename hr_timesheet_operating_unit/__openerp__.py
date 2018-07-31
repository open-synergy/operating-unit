# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "HR Timesheet with Operating Units",
    "version": "8.0.1.0.0",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "website": "https://opensynergy-indonesia.com",
    "category": "Human Resources",
    "depends": [
        "hr_timesheet_sheet",
        "hr_employee_operating_unit"
    ],
    "data": [
        "security/hr_timesheet_security.xml"
    ],
    'installable': True,
}
