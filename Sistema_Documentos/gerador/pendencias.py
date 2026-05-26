"""
Catálogo de Pendências Documentais (PD) reutilizáveis.

Cada pendência tem texto-base que pode ser usado com pequenas variações
em pareceres de Análise Documental de Reformas (PT-AD).

O gerador usa estes blocos como ponto de partida e permite override
caso o input traga conteúdo customizado.
"""

# ============================================================
# CATÁLOGO BASE DE PENDÊNCIAS PT-AD
# ============================================================

PENDENCIAS_BASE = {
    "PD-IMPER": {
        "titulo": "Impermeabilização — Procedimento Não Detalhado",
        "constatacao": (
            "O memorial prevê substituição/intervenção em área molhada, intervenção que afeta "
            "diretamente o sistema de impermeabilização, mas não descreve método de remoção, "
            "proteção ou recomposição."
        ),
        "nao_conformidade": (
            "Ausência de detalhamento técnico sobre preservação ou recomposição da "
            "impermeabilização, dos materiais previstos e da forma de proteção durante a execução."
        ),
        "exigencia": (
            "Apresentar descritivo do procedimento de impermeabilização (preservação ou recomposição), "
            "incluindo sistema, materiais, etapas executivas e cuidados com ralos, soleiras e interfaces, "
            "conforme {NBR 9575} e {NBR 9574}."
        ),
        "normas_referenciadas": ["NBR 9575", "NBR 9574"],
    },
    "PD-ESTANQ": {
        "titulo": "Teste de Estanqueidade — Ausente",
        "constatacao": (
            "Não há previsão de teste de estanqueidade após a conclusão dos serviços que afetem "
            "o sistema impermeabilizado."
        ),
        "nao_conformidade": (
            "Sem teste de estanqueidade, não há mecanismo de verificação da integridade da "
            "impermeabilização antes da reinstalação dos acabamentos e peças sanitárias."
        ),
        "exigencia": (
            "Incluir previsão de execução de teste de estanqueidade após impermeabilização ou "
            "recomposição, com registro fotográfico e/ou laudo técnico, conforme {NBR 9574}."
        ),
        "normas_referenciadas": ["NBR 9574"],
    },
    "PD-CROQUI": {
        "titulo": "Croqui da Área de Intervenção — Ausente",
        "constatacao": (
            "O memorial informa “N/A” para projetos, documentações e anexos, não apresentando "
            "croqui ou planta da área de intervenção."
        ),
        "nao_conformidade": (
            "Sem representação gráfica, não é possível localizar com segurança o escopo da reforma, "
            "ralos, peças sanitárias, box, bancada e soleiras."
        ),
        "exigencia": (
            "Apresentar croqui ou planta simples do ambiente indicando área de intervenção, "
            "posicionamento de ralos, peças sanitárias, box, bancada e soleiras."
        ),
    },
    "PD-ALVEN": {
        "titulo": "Declaração de Não Intervenção em Alvenaria Estrutural — Ausente",
        "constatacao": (
            "O empreendimento foi executado em alvenaria estrutural, sistema cujo Manual do "
            "Proprietário veda rasgos, cortes e aberturas. O memorial não contém declaração técnica "
            "expressa do responsável técnico atestando a não intervenção em alvenarias."
        ),
        "nao_conformidade": (
            "Ausência de declaração expressa impede a verificação documental do atendimento à "
            "restrição construtiva fundamental do empreendimento."
        ),
        "exigencia": (
            "Apresentar declaração técnica firmada pelo responsável técnico atestando que não "
            "haverá rasgos, cortes, aberturas, nichos ou intervenções de qualquer natureza nas "
            "alvenarias da unidade durante a execução da reforma."
        ),
    },
    "PD-ARTCMP": {
        "titulo": "Compatibilização entre ART e Escopo — Divergência",
        "constatacao": (
            "A ART indica execução de reforma de edificação com [METRAGEM] m², enquanto o memorial "
            "descreve escopo cuja área é tipicamente [INFERIOR/SUPERIOR] à metragem informada."
        ),
        "nao_conformidade": (
            "Divergência entre o escopo formalmente registrado na ART e o escopo descrito no "
            "memorial, gerando dúvida quanto à responsabilidade técnica efetivamente assumida."
        ),
        "exigencia": (
            "Compatibilizar ART e memorial — retificar, complementar ou substituir a ART de modo "
            "que a responsabilidade técnica corresponda ao escopo real da reforma."
        ),
    },
    "PD-EXEC": {
        "titulo": "Detalhamento Executivo e Plano de Obra — Insuficientes",
        "constatacao": (
            "O memorial não detalha materiais, método executivo, sequência dos serviços, proteção "
            "de prumadas, ralos e tubulações, nem plano de controle de resíduos, ruídos e proteção "
            "das áreas comuns."
        ),
        "nao_conformidade": (
            "Conteúdo insuficiente frente aos requisitos da {NBR 16280} para análise documental "
            "do plano de reforma."
        ),
        "exigencia": (
            "Apresentar memorial revisado com identificação dos materiais, método executivo, "
            "sequência dos serviços, cuidados com ralos, soleiras, rejuntes, box, bancada e bacia "
            "sanitária, e plano de controle de resíduos, ruídos, horários e proteção das áreas comuns, "
            "conforme {NBR 16280}."
        ),
        "normas_referenciadas": ["NBR 16280"],
    },
    "PD-RUIDO": {
        "titulo": "Plano de Controle de Ruídos e Horários — Ausente",
        "constatacao": (
            "O memorial não estabelece horários permitidos para execução dos serviços nem "
            "procedimentos para mitigação de ruídos."
        ),
        "nao_conformidade": (
            "A ausência deste plano descumpre o item da {NBR 16280} que exige gestão da convivência "
            "condominial durante a execução de reformas."
        ),
        "exigencia": (
            "Apresentar plano de controle de ruídos com horários autorizados pela administração "
            "condominial e procedimentos de mitigação aplicáveis a serviços ruidosos, "
            "conforme {NBR 16280}."
        ),
        "normas_referenciadas": ["NBR 16280"],
    },
    "PD-RESID": {
        "titulo": "Plano de Controle de Resíduos — Ausente",
        "constatacao": (
            "Não há descrição de plano de armazenamento, transporte e destinação dos resíduos da "
            "construção civil gerados pela reforma."
        ),
        "nao_conformidade": (
            "Ausência de plano de resíduos configura descumprimento da {NBR 16280} e da legislação "
            "municipal aplicável."
        ),
        "exigencia": (
            "Apresentar plano detalhado de gestão de resíduos contendo segregação, armazenamento "
            "provisório, transporte e destinação final, conforme exigências legais e {NBR 16280}."
        ),
        "normas_referenciadas": ["NBR 16280"],
    },
}


# ============================================================
# RESOLUÇÃO DE PLACEHOLDERS DE NORMAS
# ============================================================

def resolver_citacoes(texto: str, normas_module) -> str:
    """
    Substitui placeholders {NBR XXXX} pelo texto oficial de citação,
    consultando o catálogo de normas.

    Ex.: "...conforme {NBR 16280}" → "...conforme ABNT NBR 16280:2014"

    Args:
        texto: string com possíveis placeholders
        normas_module: módulo `normas` (passado por injeção para evitar
                       dependência circular)

    Returns:
        texto com citações resolvidas
    """
    import re
    pattern = re.compile(r"\{(NBR [\w\s\-]+?|IBAPE [^\}]+?)\}")

    def substituir(match):
        codigo = match.group(1).strip()
        try:
            return normas_module.citar(codigo)
        except KeyError:
            return f"[NORMA NÃO CATALOGADA: {codigo}]"

    return pattern.sub(substituir, texto)


def coletar_normas_usadas(pendencias_input: list) -> list[str]:
    """Coleta todos os códigos de normas referenciadas pelas pendências."""
    codigos = set()
    for item in pendencias_input:
        base = obter_pendencia_base(item["codigo_base"])
        for codigo in base.get("normas_referenciadas", []):
            codigos.add(codigo)
    return sorted(codigos)


# ============================================================
# UTILITÁRIOS
# ============================================================

def obter_pendencia_base(codigo: str) -> dict:
    """Retorna o template-base de uma pendência pelo código (PD-IMPER, etc.)."""
    if codigo not in PENDENCIAS_BASE:
        raise KeyError(f"Pendência '{codigo}' não está no catálogo. "
                       f"Disponíveis: {list(PENDENCIAS_BASE.keys())}")
    return PENDENCIAS_BASE[codigo].copy()


def mesclar_pendencia(codigo_ou_dados, override: dict = None) -> dict:
    """
    Combina pendência-base do catálogo com overrides customizados.

    Args:
        codigo_ou_dados: código (str) ou dict já completo
        override: dict com campos a sobrescrever

    Returns:
        dict com chaves: titulo, constatacao, nao_conformidade, exigencia
    """
    if isinstance(codigo_ou_dados, str):
        base = obter_pendencia_base(codigo_ou_dados)
    else:
        base = codigo_ou_dados.copy()

    if override:
        base.update({k: v for k, v in override.items() if v is not None})

    return base
