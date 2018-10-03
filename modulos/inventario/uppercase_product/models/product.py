# -*- coding: utf-8 -*-
# © 2018 - ADAX Technology
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import models, fields, api, exceptions


class uppercase_product_template(models.Model):
    _inherit = 'product.template'

    @api.onchange('name')
    def name_uppercase_templete(self):
        self.name = self.name.upper() if self.name else False

class uppercase_product(models.Model):
    _inherit = 'product.product'

    @api.onchange('name')
    def name_uppercase_product(self):
        self.name = self.name.upper() if self.name else False