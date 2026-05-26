# 📐 TEMPLATE DIAGNÓSTIKA — Padrão de Documentos Técnicos

> **Documento de referência** para o sistema automatizado de geração de pareceres, laudos e relatórios da Diagnóstika Engenharia LTDA.
>
> **Versão:** 1.0
> **Criado em:** 25/05/2026
> **Autor:** Análise consolidada a partir de 2 modelos de Parecer Técnico
> **Foco inicial:** Parecer Técnico de Análise Documental (PT-AD)

---

## 📋 Sumário

1. [Dados da Empresa](#1-dados-da-empresa)
2. [Identidade Visual](#2-identidade-visual)
3. [Sistema de Referência Interna](#3-sistema-de-referência-interna)
4. [Tipos de Documento Identificados](#4-tipos-de-documento-identificados)
5. [Estrutura Padrão (8 seções)](#5-estrutura-padrão-8-seções)
6. [Anatomia da Capa](#6-anatomia-da-capa)
7. [Headers e Footers](#7-headers-e-footers)
8. [Padrão de Tabelas e Caixas](#8-padrão-de-tabelas-e-caixas)
9. [Linguagem Técnica Padronizada](#9-linguagem-técnica-padronizada)
10. [Especificação: Parecer Técnico de Análise Documental (PT-AD)](#10-especificação-parecer-técnico-de-análise-documental-pt-ad)
11. [Inputs Necessários para Geração Automatizada](#11-inputs-necessários-para-geração-automatizada)
12. [Variáveis vs Constantes](#12-variáveis-vs-constantes)
13. [Roadmap do Sistema](#13-roadmap-do-sistema)

---

## 1. Dados da Empresa

```
Razão Social:    DIAGNÓSTIKA ENGENHARIA LTDA
CNPJ:            54.027.948/0001-60
Sede:            Campinas/SP
Função técnica:  Assessoria Técnica em Engenharia Diagnóstica
```

**Variações da função técnica observadas:**
- "Assessoria Técnica em Engenharia Diagnóstica e Análise Documental de Reformas" (PT-AD)
- "Assessoria Técnica em Engenharia Diagnóstica e Acompanhamento Técnico de Obras" (PT-NC)
- Variar conforme o tipo de documento

---

## 2. Identidade Visual

### 2.1 Logo

Localização dos assets em alta resolução:
```
C:\Users\rrcon\OneDrive\Área de Trabalho\Diagnóstika Engenharia\Marketing\Identidade Visual\
  ├─ diagnostika_logo_hd.png            (4.5 MB — alta resolução)
  ├─ Diagnostika_Engenharia_Logo (1).png
  ├─ Diagnostika_Engenharia_Simbolo.png (só ícone)
  ├─ Logo fundo escuro.png              (versão clara para fundos escuros)
  └─ diagnostika_logo_header.png        (versão para cabeçalho)
```

### 2.2 Estrutura do Logo
- **Símbolo:** ícone geométrico (forma de "D" estilizado em duas cores)
- **Wordmark:** "DIAGNÓSTIKA" (verde-petróleo, sans-serif bold) + "Engenharia" (verde-lima, peso menor)
- **Posicionamento na capa:** centralizado, no topo

### 2.3 Paleta de Cores

| Cor | Uso | Hex aproximado |
|---|---|---|
| 🟢 Verde-petróleo | Títulos principais, logo, header, footer | `#1F5F5B` |
| 🟢 Verde-lima | Acento secundário do logo, "Engenharia" | `#A8D454` |
| 🔴 Vermelho-tijolo | Cabeçalho das tabelas de PD/NC | `#A04040` |
| ⚫ Preto | Corpo de texto | `#000000` |
| 🔘 Cinza médio | Rodapés, texto auxiliar | `#666666` |
| 🟦 Azul-claro | Fundo de células de cabeçalho (tabelas) | `#E8EEF5` |
| 🟢 Verde-pálido | Fundo de caixas "Exemplo prático" | `#F0F7E8` |

### 2.4 Tipografia

- **Família:** Sans-serif (Calibri ou Arial)
- **Títulos:** Bold, verde-petróleo
- **Corpo:** Regular, preto
- **Texto em itálico:** ressalvas legais, observações

---

## 3. Sistema de Referência Interna

### 3.1 Formato

```
DK-[TIPO]-[SUBTIPO]-NNN/AAAA

Componentes:
  DK     = Diagnóstika (constante)
  TIPO   = Categoria principal (PT, LT, RT, etc.)
  SUBTIPO = Especialização (AD, NC, REF, etc.)
  NNN    = Sequencial dentro do ano (001, 002...)
  AAAA   = Ano de emissão
```

### 3.2 Tipos e Subtipos Mapeados

| Código | Tipo | Subtipo | Significado |
|---|---|---|---|
| `DK-PT-AD-NNN/AAAA` | Parecer Técnico | AD | Análise Documental (ex: reformas) |
| `DK-PT-NC-NNN/AAAA` | Parecer Técnico | NC | Não Conformidades (ex: contratos/aditivos) |
| `DK-LT-?-NNN/AAAA` | Laudo Técnico | a definir | (a mapear) |
| `DK-RT-?-NNN/AAAA` | Relatório Técnico | a definir | (a mapear) |

### 3.3 Referência de Contrato

Pareceres podem referenciar contratos da Diagnóstika:
```
DK-AAAA-NNN  (ex: DK-2025-029)
```

---

## 4. Tipos de Documento Identificados

### 4.1 Mapeados (com modelo lido)

| Código | Nome | Páginas típicas | Foco |
|---|---|---|---|
| **PT-AD** | Parecer Técnico de Análise Documental | 5-7 | Análise documental de solicitações de reforma |
| **PT-NC** | Parecer Técnico de Não Conformidades | 12+ | Análise crítica de contratos/aditivos |

### 4.2 Existentes na pasta (ainda não mapeados em detalhe)

- Laudo Técnico (vários modelos)
- Relatório Fotográfico
- Memorial Descritivo
- Notificação
- Aprovação/Reprovação de Reforma
- Vistoria Técnica
- ART (Anotação de Responsabilidade Técnica)

---

## 5. Estrutura Padrão (8 seções)

Todos os Pareceres Técnicos da Diagnóstika seguem essa estrutura:

```
┌──────────────────────────────────────────────────────────┐
│ CAPA                                                      │
│   • Logo Diagnóstika centralizado                         │
│   • Título principal (verde-petróleo, grande, bold)       │
│   • Subtítulo descritivo (verde-petróleo, médio)          │
│   • Localização: "Cliente · Cidade/UF"                    │
│   • Quadro de metadados (tabela)                          │
│   • Aviso de confidencialidade no rodapé                  │
└──────────────────────────────────────────────────────────┘
1. OBJETO E FINALIDADE
2. DOCUMENTOS ANALISADOS
3. CONTEXTO (técnico/financeiro/construtivo — varia)
4. PENDÊNCIAS / NÃO CONFORMIDADES (PD-XX ou NC-XX)
5. QUADRO RESUMO ou PREMISSAS OBRIGATÓRIAS
6. CONCLUSÃO E ENCAMINHAMENTOS
7. RESPONSABILIDADE TÉCNICA
```

---

## 6. Anatomia da Capa

### 6.1 Layout
```
┌──────────────────────────────────────┐
│                                       │
│         [LOGO DIAGNÓSTIKA]            │
│                                       │
│   PARECER TÉCNICO DE [TIPO]           │ ← H1 verde-petróleo
│   Subtítulo descritivo do caso        │ ← bold, menor
│   Cliente · Cidade/UF                  │ ← regular
│                                       │
│   ┌─────────────────────────────────┐ │
│   │ Documento       │ [valor]        │ │ ← tabela metadados
│   │ Ref. Interna    │ DK-XX-XX-NNN   │ │   (8 linhas)
│   │ Data de Emissão │ DD de mmm AAAA │ │
│   │ Elaborado por   │ Diagnóstika... │ │
│   │ Destinatário    │ [pessoa/órg]   │ │
│   │ Unidade/Caso    │ [identificação]│ │
│   │ Proprietário    │ [nome]         │ │
│   │ Revisão         │ Rev. NN — ...  │ │
│   └─────────────────────────────────┘ │
│                                       │
│   DOCUMENTO CONFIDENCIAL — USO        │ ← rodapé itálico
│   RESTRITO AO CONDOMÍNIO XXX          │
└──────────────────────────────────────┘
```

### 6.2 Metadados Obrigatórios da Capa

```yaml
documento: "Parecer Técnico de [Tipo] — [Status opcional]"
ref_interna: "DK-PT-XX-NNN/AAAA"
data_emissao: "DD de mês de AAAA"
elaborado_por: "Diagnóstika Engenharia LTDA"
destinatario: "[Pessoa/Órgão destinatário]"
unidade: "[Identificação específica — bloco, apto, condomínio]"
proprietario_ou_contrato: "[Nome do proprietário OU referência contratual]"
revisao: "Rev. NN — [tipo de revisão]"
```

---

## 7. Headers e Footers

### 7.1 Header (todas as páginas exceto capa)
```
Diagnóstika Engenharia · [Tipo do Documento] · [Cliente] · [Mês/Ano]
─────────────────────────────────────────────────────────────────
```

Exemplo:
```
Diagnóstika Engenharia · Parecer Técnico de Análise Documental de Reforma · Portal Primavera · Maio/2026
```

### 7.2 Footer (todas as páginas exceto capa)
```
┌─────────────────────────┬─────────────────────────┬──────────────┐
│ Diagnóstika Engenharia  │  [Cliente] | [Mês/Ano]  │ Página X de Y│
│ LTDA                    │                          │              │
└─────────────────────────┴─────────────────────────┴──────────────┘
```

---

## 8. Padrão de Tabelas e Caixas

### 8.1 Tabela de Pendências/Não Conformidades (PD ou NC)

Cada item segue exatamente este formato:

```
┌────────────────────────────────────────────────────────────┐
│ PD-NN  │ [Título descritivo da pendência]                  │ ← cabeçalho vermelho-tijolo
├────────────────────────────────────────────────────────────┤
│ Constatação    │ [O que foi observado / fato concreto]     │
├────────────────────────────────────────────────────────────┤
│ Não            │ [Por que isso é problema / risco]         │
│ conformidade   │                                            │
├────────────────────────────────────────────────────────────┤
│ Exigência      │ [O que deve ser feito para corrigir]      │
└────────────────────────────────────────────────────────────┘
```

### 8.2 Caixa de Exemplo Prático

Após itens críticos, aparece uma caixa com fundo verde-pálido:

```
Exemplo prático: [Texto explicativo com situação concreta para
ilustrar o ponto técnico mencionado na exigência acima.]
```

### 8.3 Quadro Resumo Final

```
┌──────┬──────────────────┬────────────────────────────┬───────────┐
│ Ref. │ Tema             │ Constatação Resumida       │ Nível     │ ← cabeçalho azul-claro
├──────┼──────────────────┼────────────────────────────┼───────────┤
│ NC-01│ [tema]           │ [resumo curto]             │ CRÍTICA   │ ← coluna nível
│ NC-02│ ...              │ ...                         │ ALTA      │   colorida
└──────┴──────────────────┴────────────────────────────┴───────────┘

Níveis observados (com cor):
  • CRÍTICA  (vermelho)
  • ALTA     (laranja)
  • MÉDIA    (amarelo)  — não observado mas previsível
  • BAIXA    (verde)    — não observado mas previsível
```

### 8.4 Tabelas Comparativas (em casos financeiros/contratuais)

Usa indicadores visuais:
```
✔  Convergente / Atende
✖  Ausente / Não atende
■  Diverge / Parcial / Atenção
```

### 8.5 Caixa de Encaminhamentos

Usada na seção 6 (Conclusão):
```
ENCAMINHAMENTOS
■ [Ação 1 a ser tomada]
■ [Ação 2 a ser tomada]
■ [Ação 3 a ser tomada]
```

### 8.6 Caixa de Conclusão

```
[Texto em destaque, fundo levemente cinza, com a decisão final
em negrito: APROVADO / NÃO APROVADO / outras categorizações]
```

---

## 9. Linguagem Técnica Padronizada

### 9.1 Aberturas comuns

- "O presente Parecer Técnico tem por objeto..."
- "Este Parecer Técnico tem por objeto a análise..."
- "A finalidade deste parecer é..."
- "Todas as constatações deste parecer são baseadas em..."

### 9.2 Estrutura PD/NC (sempre 3 partes)

```
CONSTATAÇÃO    = fato concreto observado
                 ↓
NÃO CONFORMIDADE = consequência técnica / risco
                 ↓
EXIGÊNCIA      = ação corretiva requerida
```

### 9.3 Citações de normas

- **NBR:** "ABNT NBR 16280", "ABNT NBR 6118"
- **Lei:** "Código Civil art. 618", "Lei nº X/AAAA"
- **Responsável técnico:** "Eng. [Nome] (CREA-SP NNNNNN), ART nº NNNNN"

### 9.4 Conclusões

- "A Diagnóstika Engenharia conclui que..."
- "Recomenda-se..."
- "Não deve ser assinado na forma atualmente apresentada"
- "Encontra-se NÃO APROVADA neste momento"

### 9.5 Ressalvas obrigatórias

Sempre presentes:
- Limitação ao escopo documental (não substitui aprovações de órgãos públicos)
- Distinção entre análise documental ≠ viabilidade técnica
- Não responsabilidade por decisões tomadas sem observância
- Possibilidade de reanálise mediante complementações

### 9.6 Estilo geral

- Terceira pessoa, voz passiva quando apropriado
- Formal, técnica, sem floreios
- Frases médias (15-25 palavras)
- Negrito SOMENTE em pontos-chave (decisões, valores, prazos)

---

## 10. Especificação: Parecer Técnico de Análise Documental (PT-AD)

> **Este é o primeiro tipo a ser automatizado.**

### 10.1 Gatilho de Geração

Solicitação típica:
- Síndica (ex: Camila) reporta solicitação de reforma de um morador
- Documentação chega via WhatsApp ou MegaZap
- Inclui: memorial descritivo, ART, plantas/croquis (se houver)

### 10.2 Estrutura Específica do PT-AD

```
CAPA
1. OBJETO E FINALIDADE
   • Identifica unidade, proprietário, responsável técnico (CREA + ART)
   • Cita: Manual do Proprietário + ABNT NBR 16280

2. DOCUMENTOS ANALISADOS
   • Memorial Descritivo / Plano de Reforma
   • ART
   • Manual do Proprietário do empreendimento
   • ABNT NBR 16280

3. ESCOPO DECLARADO E SISTEMA CONSTRUTIVO
   • Sistema construtivo (alvenaria estrutural ou convencional)
   • Ambiente da reforma (banheiro, sala, etc.)
   • Serviços declarados (lista)
   • Prazo
   • ART (m² declarado)

4. PENDÊNCIAS DOCUMENTAIS IDENTIFICADAS
   • Padrão recorrente de pendências (ver lista 10.3)

5. QUADRO RESUMO
   • Tabela consolidada: Ref / Tema / Pendência

6. CONCLUSÃO E ENCAMINHAMENTOS
   • Status: APROVADO / NÃO APROVADO
   • Ressalva: análise documental ≠ impossibilidade técnica
   • Caixa de Encaminhamentos

7. RESPONSABILIDADE TÉCNICA
   • Padrão Diagnóstika
```

### 10.3 Catálogo de Pendências Recorrentes (PT-AD)

Pendências comuns em análise de reformas:

| Código sugerido | Tema | Quando aplicar |
|---|---|---|
| PD-IMPER | Impermeabilização — Procedimento não detalhado | Reformas em áreas molhadas (banheiros, cozinhas) |
| PD-ESTANQ | Teste de Estanqueidade — Ausente | Após qualquer mexer em impermeabilização |
| PD-CROQUI | Croqui da Área de Intervenção — Ausente | Quando memorial não tem representação gráfica |
| PD-ALVEN | Declaração de Não Intervenção em Alvenaria Estrutural | Empreendimentos em alvenaria estrutural |
| PD-ARTCMP | Compatibilização ART × Escopo | Quando m² ou descrição diverge entre ART e memorial |
| PD-EXEC | Detalhamento Executivo e Plano de Obra — Insuficiente | Memoriais genéricos sem método executivo |
| PD-RUIDO | Plano de Controle de Ruídos e Horários | Sempre que aplicável (NBR 16280) |
| PD-RESID | Plano de Controle de Resíduos | Sempre que aplicável (NBR 16280) |
| PD-PROTEC | Proteção de Áreas Comuns | Sempre que houver passagem por áreas comuns |
| PD-PRAZO | Compatibilidade de Prazo com Escopo | Quando prazo declarado parece subdimensionado |

---

## 11. Inputs Necessários para Geração Automatizada

### 11.1 Estrutura JSON sugerida (entrada do gerador)

```json
{
  "documento": {
    "tipo": "PT-AD",
    "ref_sequencial": 1,
    "ano": 2026,
    "data_emissao": "2026-05-25",
    "revisao": "Rev. 00 — Emissão inicial"
  },
  "cliente": {
    "razao_social_ou_nome": "Condomínio Portal Primavera",
    "cidade_uf": "Campinas/SP",
    "cnpj": "XX.XXX.XXX/XXXX-XX",
    "destinatario": "Administração do Condomínio Portal Primavera"
  },
  "caso": {
    "tipo_solicitacao": "Solicitação de Reforma",
    "unidade": "Bloco 07 — Apartamento 304",
    "proprietario": "Lucas Salles dos Santos",
    "responsavel_tecnico": {
      "nome": "Eng. Guilherme Calixto de Oliveira",
      "crea": "CREA-SP 5070087371",
      "art": "2620261607007"
    },
    "ambiente": "Banheiro",
    "sistema_construtivo": "Alvenaria estrutural",
    "servicos_declarados": [
      "Substituição de piso",
      "Substituição de bacia sanitária",
      "Substituição de vidro do box",
      "Substituição de mármore da bancada",
      "Substituição de porta"
    ],
    "prazo_declarado": "21 dias",
    "art_metragem": "52 m²"
  },
  "documentos_analisados": [
    {
      "ref": "i",
      "nome": "Memorial Descritivo / Plano de Reforma",
      "descricao": "Descrição dos serviços pretendidos no banheiro da unidade."
    },
    {
      "ref": "ii",
      "nome": "ART nº 2620261607007",
      "descricao": "Anotação de Responsabilidade Técnica — execução de reforma de edificação, 52 m²."
    },
    {
      "ref": "iii",
      "nome": "Manual do Proprietário — Portal Primavera",
      "descricao": "Diretrizes para reformas e restrições construtivas (alvenaria estrutural)."
    },
    {
      "ref": "iv",
      "nome": "ABNT NBR 16280",
      "descricao": "Reforma em edificações — Sistema de gestão de reformas."
    }
  ],
  "pendencias": [
    {
      "codigo": "PD-01",
      "titulo": "Impermeabilização — Procedimento Não Detalhado",
      "constatacao": "O memorial prevê substituição do piso do banheiro...",
      "nao_conformidade": "Ausência de detalhamento técnico sobre...",
      "exigencia": "Apresentar descritivo do procedimento de..."
    }
    // ... outras pendências
  ],
  "quadro_resumo": [
    {"ref": "PD-01", "tema": "Impermeabilização", "pendencia": "Procedimento não detalhado"}
    // ...
  ],
  "conclusao": {
    "status": "NÃO APROVADO",  // ou "APROVADO" / "APROVADO COM RESSALVAS"
    "encaminhamentos": [
      "Não autorizar o início dos serviços...",
      "Encaminhar este parecer ao proprietário...",
      "Submeter a documentação complementar..."
    ]
  }
}
```

### 11.2 Dados que vêm do banco de demandas (catalogador)

- Nome do solicitante (síndica, morador, etc.)
- Descrição da solicitação
- Data
- Documentos anexados
- Vínculo com relatório fotográfico do Claudemir (se houver)

### 11.3 Dados que vêm do banco de normas

- NBR aplicável conforme tipo de problema
- Texto-base da norma para citação
- Restrições construtivas do Manual do Proprietário do condomínio

---

## 12. Variáveis vs Constantes

### 12.1 CONSTANTES (sempre iguais)

- Razão Social: "DIAGNÓSTIKA ENGENHARIA LTDA"
- CNPJ: "54.027.948/0001-60"
- Sede: "Campinas/SP"
- Logo (arquivo de imagem)
- Paleta de cores
- Tipografia
- Estrutura das 8 seções
- Texto de ressalvas legais (com pequenas variações por tipo)
- Header e footer
- Função técnica de assinatura

### 12.2 VARIÁVEIS POR DOCUMENTO

- Ref. Interna (NNN incremental por ano e tipo)
- Cliente / Condomínio
- Destinatário
- Unidade/Caso
- Data
- Lista de documentos analisados
- Contexto técnico/financeiro
- Lista de pendências (conteúdo livre, mas estrutura fixa)
- Status da conclusão
- Encaminhamentos

### 12.3 BIBLIOTECA DE TEMPLATES REUTILIZÁVEIS

Para escalar, manter biblioteca de:
- Pendências recorrentes (PD-IMPER, PD-ESTANQ, etc.) com texto-base
- Citações de normas (texto curto da NBR)
- Frases-padrão (aberturas, conclusões, ressalvas)
- Quadros pré-formatados

---

## 13. Roadmap do Sistema

### Fase 1 — Catalogador (em construção)
- ✅ Setup do ambiente (Claude Code CLI + Playwright + Remote Control)
- ⏳ Leitura de mensagens da Camila (WhatsApp)
- ⏳ Leitura do grupo Engenharia Primavera
- ⏳ Catalogação: cada mensagem-pedido vira uma "demanda" estruturada
- ⏳ Transcrição de áudios (Whisper small já instalado)

### Fase 2 — Catalogador de Relatórios Fotográficos
- ⏳ Leitura do grupo Portal Primavera-Diagnostika
- ⏳ Download e organização das fotos por data
- ⏳ Vínculo demanda ↔ relatório fotográfico (por data/contexto)

### Fase 3 — Indexador de Normas
- ⏳ Catalogar pasta `Normas/` (9 NBRs já presentes)
- ⏳ Mapear tipo-de-problema → NBR aplicável
- ⏳ Extrair trechos relevantes para citação

### Fase 4 — Gerador de PT-AD (primeiro tipo)
- ⏳ Implementar Python com `python-docx`
- ⏳ Template base com logo, cores, headers, footers
- ⏳ Função `gerar_pt_ad(input_json) → arquivo.docx`
- ⏳ Numeração sequencial automática
- ⏳ Conversão para PDF (opcional, via LibreOffice ou similar)

### Fase 5 — Testes com Casos Reais
- ⏳ Gerar 3 PT-AD a partir de dados reais do banco de demandas
- ⏳ Comparar com pareceres feitos manualmente pelo Rogério
- ⏳ Ajustar template até qualidade aceitável

### Fase 6 — Expansão para outros tipos
- ⏳ Adicionar suporte a PT-NC
- ⏳ Adicionar suporte a Laudos Técnicos
- ⏳ Adicionar suporte a Relatórios de Vistoria
- ⏳ Adicionar suporte a Notificações

### Fase 7 — Interface de Uso
- ⏳ CLI simples para gerar um documento por comando
- ⏳ Eventualmente: interface web ou integração com Sistema Financeiro

---

## 📂 Arquivos de Referência (analisados)

1. **PT-AD modelo:** `Clientes/Primavera/Laudos e Pareceres/Parecer_Tecnico_Portal_Primavera_Bl07_Apt304.pdf` (5 páginas, DK-PT-AD-001/2026)
2. **PT-NC modelo:** `Clientes/Condomínio Edifício Menotti del Picchia/AAM Engenharia/Aditivo Contratual/Parecer_Nao_Conformidades_Aditivo_AAM_Mai2026.pdf` (12 páginas, DK-PT-NC-001/2026)

## 🔗 Próximos Documentos a Analisar

- Laudo Técnico (LAUDO_TECNICO_CAIXAS D'ÁGUA PRIMAVERA.pdf — 45 páginas)
- Notificação (NOTIFICAÇÃO_Reforma_Sem_Autorização_Bloco_12_Apto_101.docx)
- Modelo explícito (Modelo_Relatorio_Diagnostika Salao festa.pdf)
- Anexo Catálogo Fotográfico (Anexo III FMP PP 00126 Catálogo_Fotográfico.pdf)

---

**Fim do documento — Versão 1.0**
