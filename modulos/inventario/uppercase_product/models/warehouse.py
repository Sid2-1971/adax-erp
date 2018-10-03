# -*- coding: utf-8 -*-
# © 2018 - ADAX Technology
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import models, fields, api, exceptions


class uppercase_stock_warehouse(models.Model):
    _inherit = "stock.warehouse"

    @api.onchange('name')
    def name_uppercase_warehouse(self):
        self.name = self.name.upper() if self.name else False

    @api.onchange('code')
    def code_uppercase_warehouse(self):
        self.code = self.code.upper() if self.code else False
