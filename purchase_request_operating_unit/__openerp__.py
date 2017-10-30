# -*- coding: utf-8 -*-
# © 2015 Eficent Business and IT Consulting Services S.L. -
# Jordi Ballester Alomar
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Operating Unit in Purchase Requests",
    "version": "8.0.1.0.0",
    "author": "Eficent, Odoo Community Association (OCA)",
    "website": "http://www.eficent.com",
    "category": "Purchase Management",
    "depends": ["purchase_request",
                "purchase_operating_unit"],
    "data": [
        "view/purchase_request_view.xml",
        "security/purchase_security.xml",
    ],
    "license": "AGPL-3",
    'installable': True,
}
