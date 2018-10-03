# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    resource_ids = fields.One2many(
        'resource.resource', 'user_id', 'Recursos')
    resource_calendar_id = fields.Many2one(
        'resource.calendar', 'Horas de trabalho padrão',
        related='resource_ids.calendar_id')
