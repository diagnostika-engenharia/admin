"""
Estilos visuais Diagnóstika Engenharia.

Define paleta de cores, fontes e tamanhos padrão para uso no gerador de documentos.
Baseado na análise consolidada em TEMPLATE_DIAGNOSTIKA.md.
"""

from docx.shared import RGBColor, Pt, Cm


# ============================================================
# PALETA DE CORES DIAGNÓSTIKA
# ============================================================

VERDE_PETROLEO = RGBColor(0x1F, 0x5F, 0x5B)   # Títulos, headers, footers
VERDE_LIMA = RGBColor(0xA8, 0xD4, 0x54)        # Acento secundário (Engenharia)
VERMELHO_TIJOLO = RGBColor(0xA0, 0x40, 0x40)   # Cabeçalho tabelas PD/NC
PRETO = RGBColor(0x00, 0x00, 0x00)             # Corpo
CINZA_MEDIO = RGBColor(0x66, 0x66, 0x66)       # Texto auxiliar, rodapé
AZUL_CLARO_TABELA = "E8EEF5"                    # Fundo cabeçalho tabelas (hex sem #)
VERDE_PALIDO_EXEMPLO = "F0F7E8"                # Fundo caixas "Exemplo prático"
CINZA_CLARO_BG = "F5F5F5"                       # Fundo caixas neutras
LARANJA_ALTA = RGBColor(0xE8, 0x8B, 0x00)      # Nível "ALTA"


# ============================================================
# TIPOGRAFIA
# ============================================================

FONTE_PADRAO = "Calibri"

TAM_TITULO_CAPA = Pt(22)        # PARECER TÉCNICO DE...
TAM_SUBTITULO_CAPA = Pt(14)     # Subtítulo descritivo
TAM_LOCAL_CAPA = Pt(11)         # Cliente · Cidade/UF
TAM_TITULO_SECAO = Pt(14)       # 1. OBJETO E FINALIDADE
TAM_SUBTITULO_SECAO = Pt(11)    # PD-01 [título]
TAM_CORPO = Pt(10)              # Texto comum
TAM_TABELA = Pt(9)              # Texto em tabelas
TAM_HEADER_FOOTER = Pt(8)       # Cabeçalho/rodapé
TAM_RESSALVA = Pt(9)            # Texto em itálico final


# ============================================================
# MARGENS DA PÁGINA
# ============================================================

MARGEM_SUPERIOR = Cm(2.0)
MARGEM_INFERIOR = Cm(2.0)
MARGEM_ESQUERDA = Cm(2.5)
MARGEM_DIREITA = Cm(2.0)


# ============================================================
# DADOS FIXOS DA EMPRESA (CONSTANTES)
# ============================================================

EMPRESA = {
    "razao_social": "DIAGNÓSTIKA ENGENHARIA LTDA",
    "cnpj": "54.027.948/0001-60",
    "cidade": "Campinas",
    "uf": "SP",
    "cidade_uf": "Campinas/SP",
}


# ============================================================
# TEXTOS PADRONIZADOS (REUSO)
# ============================================================

RESSALVA_PT_AD = (
    "Este parecer foi elaborado com base exclusivamente nos documentos formalmente apresentados, "
    "limitando-se à análise técnica de conformidade documental do plano de reforma frente ao "
    "Manual do Proprietário e à ABNT NBR 16280, não substituindo eventuais aprovações ou licenças "
    "exigíveis junto a órgãos públicos competentes, nem constituindo manifestação sobre a viabilidade "
    "técnica integral dos serviços, cuja responsabilidade permanece com o profissional habilitado "
    "contratado pelo proprietário."
)

FUNCAO_TECNICA_PT_AD = "Assessoria Técnica em Engenharia Diagnóstica e Análise Documental de Reformas"
FUNCAO_TECNICA_PT_NC = "Assessoria Técnica em Engenharia Diagnóstica e Acompanhamento Técnico de Obras"

AVISO_CONFIDENCIAL = "DOCUMENTO CONFIDENCIAL — USO RESTRITO AO {destinatario_curto}"


# ============================================================
# CONFIG GERAL DO DOCUMENTO
# ============================================================

CONFIG = {
    "tamanho_pagina": "A4",
    "orientacao": "portrait",
    "altura_logo_capa_cm": 4.0,
    "espacamento_paragrafos_pt": 4,
    "espacamento_linhas": 1.15,
}
