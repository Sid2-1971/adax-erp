# -*- coding: utf-8 -*-

from odoo import api, fields, models

class DocumentSettings(models.TransientModel):
    
    _inherit = 'res.config.settings'
    
    module_muk_dms_access = fields.Boolean(
        string="Controle de acesso",
        help="Permite a criação de grupos para definir direitos de acesso.")
    
    module_muk_dms_attachment = fields.Boolean(
        string="Localização de armazenamento de anexos",
        help="Permite que anexos sejam armazenados dentro de documentos do Arquivo.")
    
    module_muk_dms_attachment_rules = fields.Boolean(
        string="Regras de armazenamento de anexos",
        help="Permite que os anexos sejam colocados automaticamente no diretório correto.")
    
    module_muk_dms_finder = fields.Boolean(
        string="Localizador",
        help="Ativa o localizador de documentos.")
    
    module_muk_dms_file = fields.Boolean(
        string="Loja de arquivos",
        help="Ativa uma nova opção de salvamento para armazenar arquivos em um armazenamento de arquivos.")
    
    module_muk_dms_lobject = fields.Boolean(
        string="Objetos grandes ",
        help="Ativa uma nova opção de salvamento para armazenar arquivos em objetos grandes.")
    
    max_upload_size = fields.Char(
        string="Tamanho",
        help="Define o tamanho máximo de upload em MB. Padrão (25MB)")
    
    forbidden_extensions = fields.Char(
        string="Extensões",
        help="Define uma lista de extensões de arquivos proibidos. (Exemplo: '.exe, .msi')")
    
    @api.model
    def get_values(self):
        res = super(DocumentSettings, self).get_values()
        get_param = self.env['ir.config_parameter'].sudo().get_param
        res.update(
            max_upload_size=get_param('muk_dms.max_upload_size', default="25"),
            forbidden_extensions=get_param('muk_dms.forbidden_extensions', default=""),
        )
        return res
        
    def set_values(self):
        config = self.env['ir.config_parameter']
        get_param = config.sudo().get_param
        set_param = config.sudo().set_param
        max_upload_size = get_param('muk_dms.max_upload_size', default="25"),
        forbidden_extensions = get_param('muk_dms.forbidden_extensions', default=""),
        if self.max_upload_size and self.max_upload_size != max_upload_size:
            if not self.user_has_groups('muk_dms.group_dms_admin'):
                raise AccessDenied()
            set_param('muk_dms.max_upload_size', self.max_upload_size or "25")
        if self.forbidden_extensions and self.forbidden_extensions != forbidden_extensions:
            if not self.user_has_groups('muk_dms.group_dms_admin'):
                raise AccessDenied()
            set_param('muk_dms.forbidden_extensions', self.forbidden_extensions or "")
        super(DocumentSettings, self).set_values()