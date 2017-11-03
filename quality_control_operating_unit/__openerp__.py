# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Quality Control Operating Unit",
    "version": "8.0.0.0.0",
    "license": 'AGPL-3',
    "author": "OpenSynergy Indonesia, "
              "Odoo Community Association (OCA)",
    "website": "https://opensynergy-indonesia.com",
    "category": "Manufacturing",
    "depends": [
        "quality_control",
        "operating_unit",
    ],
    "data": [
        "views/quality_control_views.xml",
        "security/quality_control_security.xml"
    ],
    'installable': True,
}
