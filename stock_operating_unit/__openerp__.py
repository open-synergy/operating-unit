# -*- coding: utf-8 -*-
# © 2015 Eficent Business and IT Consulting Services S.L. -
# Jordi Ballester Alomar
# © 2015 Serpent Consulting Services Pvt. Ltd. - Sudhir Arya
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Stock with Operating Units",
    "summary": "An operating unit (OU) is an organizational entity part of a\
        company",
    "version": "8.0.1.2.0",
    "category": "Generic Modules/Sales & Purchases",
    "license": "AGPL-3",
    "author": "Eficent, Serpent Consulting Services Pvt. Ltd., "
              "Odoo Community Association (OCA)",
    "website": "http://www.eficent.com",
    "depends": ["stock", "account_operating_unit"],
    "data": [
        "security/stock_security.xml",
        "data/stock_data.xml",
        "view/stock.xml",
        "view/stock_inventory_views.xml",
    ],
    "demo": [
        "demo/stock_demo.xml",
    ],
    "installable": True,
}
