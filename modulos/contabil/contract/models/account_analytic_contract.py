# -*- coding: utf-8 -*-
from odoo import api, fields, models


class AccountAnalyticContract(models.Model):
    _name = 'account.analytic.contract'

    # These fields will not be synced to the contract
    NO_SYNC = [
        'name',
        'partner_id',
    ]

    name = fields.Char(
        required=True,
    )
    # Needed for avoiding errors on several inherited behaviors
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Parceiro (sempre falso)",
    )
    pricelist_id = fields.Many2one(
        comodel_name='product.pricelist',
        string='Lista de preços',
    )
    recurring_invoice_line_ids = fields.One2many(
        comodel_name='account.analytic.contract.line',
        inverse_name='analytic_account_id',
        copy=True,
        string='Linhas da fatura',
    )
    recurring_rule_type = fields.Selection(
        [('daily', 'Dia(s)'),
         ('weekly', 'Semana(s)'),
         ('monthly', 'Mês(es)'),
         ('monthlylastday', 'Último dia do mês'),
         ('yearly', 'Ano(s)'),
         ],
        default='monthly',
        string='Recorrência',
        help="Especifique o intervalo para geração automática de faturas.",
    )
    recurring_invoicing_type = fields.Selection(
        [('pre-paid', 'Pré-pago'),
         ('post-paid', 'Pós-pago'),
         ],
        default='pre-paid',
        string='Tipo de faturamento',
        help="Especifique se a data do processo é 'de' ou 'para' data de faturamento",
    )
    recurring_interval = fields.Integer(
        default=1,
        string='Repete a cada',
        help="Repete a cada (dias / semana / mês / ano)",
    )
    journal_id = fields.Many2one(
        'account.journal',
        string='Diário',
        default=lambda s: s._default_journal(),
        domain="[('type', '=', 'sale'),('company_id', '=', company_id)]",
    )
    company_id = fields.Many2one(
        'res.company',
        string='Empresa',
        required=True,
        default=lambda self: self.env.user.company_id,
    )

    @api.model
    def _default_journal(self):
        company_id = self.env.context.get(
            'company_id', self.env.user.company_id.id)
        domain = [
            ('type', '=', 'sale'),
            ('company_id', '=', company_id)]
        return self.env['account.journal'].search(domain, limit=1)
