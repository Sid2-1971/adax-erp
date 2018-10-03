# -*- coding: utf-8 -*-
# © 2018 - ADAX Technology
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import models, fields, api, exceptions


class uppercase_partner(models.Model):
    _inherit = 'res.partner'

    @api.onchange('name')
    def name_uppercase_partner(self):
        self.name = self.name.upper() if self.name else False