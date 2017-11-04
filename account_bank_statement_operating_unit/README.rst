.. image:: https://img.shields.io/badge/license-AGPLv3-blue.svg
   :target: https://www.gnu.org/licenses/agpl.html
   :alt: License: AGPL-3

===========================================
Encode Bank Statements with Operating Units
===========================================

Adds the Operating Unit (OU) to the Bank Statement.

The Bank Statement OU is defaulted to the OU of the user.

Accounting entries generated from the Bank Transactions will be handled as follows:

- The entry representing the money in/out will be set to the OU of the Bank Statement.
- The counterparty entry/entries will be defaulted to the OU of the Bank Statement.
  This default can be changed manually via the "reconcile" widget,
  e.g. to assign banks costs to multiple Organisation Units.

Usage
=====


.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/213/8.0

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/OCA/operating-unit/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed feedback.

Credits
=======

Images
------

* Odoo Community Association: `Icon <https://github.com/OCA/maintainer-tools/blob/master/template/module/static/description/icon.svg>`_.

Contributors
------------

* Noviat
* OpenSynergy Indonesia <https://opensynergy-indonesia.com>

Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit https://odoo-community.org.
