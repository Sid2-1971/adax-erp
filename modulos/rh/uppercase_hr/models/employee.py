# -*- coding: utf-8 -*-
# © 2018 - ADAX Technology
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import models, fields, api, exceptions


class uppercase_employee(models.Model):
    _inherit = 'hr.employee'

    @api.onchange('name')
    def name_uppercase_employee(self):
        self.name = self.name.upper() if self.name else False

class uppercase_department(models.Model):
    _inherit = 'hr.department'

    @api.onchange('name')
    def name_uppercase_department(self):
        self.name = self.name.upper() if self.name else False


