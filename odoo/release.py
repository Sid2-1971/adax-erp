# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

RELEASE_LEVELS = [ALPHA, BETA, RELEASE_CANDIDATE, FINAL] = ['alpha', 'beta', 'candidate', 'final']
RELEASE_LEVELS_DISPLAY = {ALPHA: ALPHA,
                          BETA: BETA,
                          RELEASE_CANDIDATE: 'rc',
                          FINAL: ''}

# version_info format: (MAJOR, MINOR, MICRO, RELEASE_LEVEL, SERIAL)
# inspired by Python's own sys.version_info, in order to be
# properly comparable using normal operarors, for example:
#  (6,1,0,'beta',0) < (6,1,0,'candidate',1) < (6,1,0,'candidate',2)
#  (6,1,0,'candidate',2) < (6,1,0,'final',0) < (6,1,2,'final',0)
version_info = (' ' , ' ' ,' ', FINAL, ' ', ' ')
version = '.'.join(str(s) for s in version_info[:2]) + RELEASE_LEVELS_DISPLAY[version_info[3]] + str(version_info[4] or '') + version_info[5]
series = serie = major_version = '.'.join(str(s) for s in version_info[:2])

product_name = 'ADAX ERP'
description = 'ADAX-ERP Server'
long_desc = '''O ADAX-ERP é um completo ERP e CRM. As principais características são a contabilidade (analítica
e financeira), gestão de estoque, gestão de vendas e compras, tarefas
automação, campanhas de marketing, help desk, PPDV, etc. As características técnicas incluem
um servidor distribuído, um banco de dados de objetos, uma GUI dinâmica,
relatórios personalizáveis ​​e interfaces XML-RPC.
'''
classifiers = """Situação do Desenvolvimento - Produção/Estável

Linguagem de Desenvolvimento :: Python
"""
url = 'https://www.adaxtechnology.com'
author = 'ADAX Technology'
author_email = 'contato@adaxtechnology.com'
license = 'LGPL-3'

nt_service_name = "odoo-server-" + series.replace('~','-')
