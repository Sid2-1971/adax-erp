# -*- coding: utf-8 -*-

from odoo import models, fields


class ResPartnerWhatsapp(models.Model):
    _inherit = 'res.partner'

    mobile_whatsapp_link = fields.Html(compute='compute_mobile_whatsapp_link')

    def compute_mobile_whatsapp_link(self):
        for record in self:
            body = ''

            if record.mobile:
                body = """
                <a target="_blank" href="https://api.whatsapp.com/send?phone=%s">
                    <i class="fa fa-whatsapp"/> <span class="hidden-lg hidden-xl">Enviar mensagem via WhatsApp</span>
                </a>
                """ % record.mobile
            record.mobile_whatsapp_link = body
