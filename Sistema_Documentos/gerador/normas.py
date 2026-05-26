"""
Módulo de gestão de normas técnicas.

Carrega normas_catalogo.json, fornece API para consulta e
emite alertas quando uma norma está marcada como pendente
de verificação ou potencialmente desatualizada.

REGRA FIRME: nenhum documento gerado pode citar uma norma sem
que ela esteja no catálogo. Tentativas de uso de código não
registrado lançam exceção.
"""

import json
from pathlib import Path
from typing import Optional


# ============================================================
# CARREGAMENTO DO CATÁLOGO
# ============================================================

_CACHE_CATALOGO = None


def carregar_catalogo(caminho: Path = None) -> dict:
    """Carrega normas_catalogo.json (com cache)."""
    global _CACHE_CATALOGO
    if _CACHE_CATALOGO is not None and caminho is None:
        return _CACHE_CATALOGO

    if caminho is None:
        caminho = Path(__file__).parent / "normas_catalogo.json"

    if not caminho.exists():
        raise FileNotFoundError(f"Catálogo de normas não encontrado: {caminho}")

    with open(caminho, "r", encoding="utf-8") as f:
        catalogo = json.load(f)

    _CACHE_CATALOGO = catalogo
    return catalogo


# ============================================================
# CONSULTAS
# ============================================================

def obter_norma(codigo: str) -> dict:
    """
    Retorna os dados completos de uma norma do catálogo.

    Args:
        codigo: ex. 'NBR 16280', 'NBR 9575', 'IBAPE Inspeção Predial'

    Returns:
        dict com os dados da norma

    Raises:
        KeyError: se o código não estiver no catálogo
    """
    catalogo = carregar_catalogo()
    if codigo not in catalogo or codigo.startswith("_"):
        disponiveis = [k for k in catalogo.keys() if not k.startswith("_")]
        raise KeyError(
            f"Norma '{codigo}' não está no catálogo registrado.\n"
            f"Normas registradas: {disponiveis}\n"
            f"Adicione a norma em 'normas_catalogo.json' antes de citá-la."
        )
    return catalogo[codigo]


def citar(codigo: str) -> str:
    """
    Retorna a citação oficial pronta para uso em texto.

    Exemplo: citar('NBR 9575') -> 'ABNT NBR 9575:2010'
    """
    norma = obter_norma(codigo)
    return norma["citacao_oficial"]


def status_norma(codigo: str) -> str:
    """Retorna o status da norma (vigente_confirmada / verificacao_pendente / etc)."""
    return obter_norma(codigo).get("status", "verificacao_pendente")


def precisa_verificar(codigo: str) -> bool:
    """True se a norma exige verificação antes de ser citada com segurança."""
    return status_norma(codigo) != "vigente_confirmada"


def alertas_para_pareceres(codigos_usados: list[str]) -> list[dict]:
    """
    Dada a lista de normas que um parecer vai citar, retorna a lista de
    alertas (se houver) para que o gerador inclua/destaque no documento.

    Cada alerta tem: codigo, status, observacao_para_revisao.
    """
    alertas = []
    for codigo in codigos_usados:
        try:
            norma = obter_norma(codigo)
        except KeyError as e:
            alertas.append({
                "codigo": codigo,
                "status": "ausente_do_catalogo",
                "severidade": "BLOQUEANTE",
                "mensagem": str(e),
            })
            continue

        status = norma.get("status", "verificacao_pendente")
        if status == "vigente_confirmada":
            continue

        severidade = {
            "verificacao_pendente": "MEDIA",
            "potencialmente_desatualizada": "ALTA",
            "revogada": "CRITICA",
        }.get(status, "MEDIA")

        alertas.append({
            "codigo": codigo,
            "status": status,
            "severidade": severidade,
            "citacao_atual": norma.get("citacao_oficial", "?"),
            "observacao": norma.get("observacoes", ""),
            "acao_requerida": norma.get("acao_requerida", "Verificar versão vigente no catálogo ABNT."),
        })

    return alertas


# ============================================================
# UTILITÁRIO: imprimir relatório de status
# ============================================================

def relatorio_status_catalogo() -> str:
    """Imprime relatório resumido do catálogo (status de cada norma)."""
    catalogo = carregar_catalogo()
    linhas = ["=" * 70, "RELATÓRIO DE STATUS DAS NORMAS", "=" * 70]
    for codigo, dados in catalogo.items():
        if codigo.startswith("_"):
            continue
        status = dados.get("status", "?")
        marker = {
            "vigente_confirmada": "[OK] ",
            "verificacao_pendente": "[??] ",
            "potencialmente_desatualizada": "[!!] ",
            "revogada": "[XX] ",
        }.get(status, "[?]  ")
        cit = dados.get("citacao_oficial", "?")
        linhas.append(f"{marker}{codigo:<25} {cit:<28} {status}")
    linhas.append("=" * 70)
    return "\n".join(linhas)


if __name__ == "__main__":
    print(relatorio_status_catalogo())
