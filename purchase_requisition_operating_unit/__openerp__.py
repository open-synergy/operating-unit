# -*- coding: utf-8 -*-
# © 2015 Eficent Business and IT Consulting Services S.L. -
# Jordi Ballester Alomar
# © 2015 Serpent Consulting Services Pvt. Ltd. - Sudhir Arya
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Operating Unit in Purchase Requisitions",
    "version": "8.0.1.0.0",
    "author": "Eficent, Serpent Consulting Services Pvt. Ltd.,"
              "Odoo Community Association (OCA)",
    "website": "http://www.eficent.com",
    "category": "Purchase Management",
    "license": "AGPL-3",
    "depends": ["purchase_requisition",
                "purchase_operating_unit"],
    "data": [
        "view/purchase_requisition.xml",
        "security/purchase_security.xml",
    ],
    'installable': True,
}
