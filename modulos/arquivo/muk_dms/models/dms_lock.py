# -*- coding: utf-8 -*-

import logging

from odoo import models, api, fields

_logger = logging.getLogger(__name__)

class Lock(models.Model):
    _name = 'muk_dms.lock'
    _description = "Bloqueio de diretório ou arquivo"

    name = fields.Char(
        compute='_compute_name',
        string="Nome")

    locked_by = fields.Char(
        string="Bloqueado por",
        required=True)
    
    locked_by_ref = fields.Reference(
        [('res.users', 'User')],
        string="Referência do usuário")

    lock_ref = fields.Reference(
        [],
        string="Referência de Objeto",
        required=True)
    
    token = fields.Char(
        string="Token")
    
    operation = fields.Char(
        string="Operação")
    
    @api.one
    @api.depends('lock_ref')
    def _compute_name(self):
        self.name = "Bloqueio para " + str(self.lock_ref.name)