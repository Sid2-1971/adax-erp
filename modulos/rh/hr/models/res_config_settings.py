# -*- coding: utf-8 -*-

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    resource_calendar_id = fields.Many2one(
        'resource.calendar', 'Horário de trabalho da empresa',
        related='company_id.resource_calendar_id')
    module_hr_org_chart = fields.Boolean(string="Mostrar organograma")
