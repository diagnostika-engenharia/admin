# 🏗️ Gerador de Documentos Diagnóstika

> Sistema automatizado de geração de pareceres técnicos no padrão visual e estrutural Diagnóstika Engenharia.

## 🎯 Status atual

**Versão 0.1 — MVP funcional para PT-AD**

✅ Suporte completo: **Parecer Técnico de Análise Documental (PT-AD)**
⏳ Em planejamento: PT-NC, Laudo Técnico, Relatório Técnico

## 📦 Estrutura

```
gerador/
├── README.md              ← este arquivo
├── requirements.txt       ← dependências Python
├── gerar_pt_ad.py         ← script principal
├── estilos.py             ← paleta de cores, fontes, dados da empresa
├── pendencias.py          ← catálogo reutilizável de PDs
├── assets/
│   └── logo.png           ← logo Diagnóstika (alta resolução)
├── inputs/
│   └── exemplo_apt304.json ← caso de teste
└── saidas/                ← documentos .docx gerados
```

## 🚀 Como usar

### Pré-requisitos

- Python 3.10+ instalado
- python-docx instalado (`pip install python-docx`)

### Gerar um documento de exemplo

```powershell
# Caminho do Python (já confirmado nesta máquina)
$py = "C:\Users\rrcon\AppData\Local\Programs\Python\Python312\python.exe"

# Navegar para a pasta
cd "C:\Users\rrcon\OneDrive\Área de Trabalho\Diagnóstika Engenharia\Admin Diagnostika\Sistema_Documentos\gerador"

# Rodar com o exemplo
& $py gerar_pt_ad.py inputs/exemplo_apt304.json
```

Resultado: arquivo `.docx` em `saidas/`.

### Gerar com input customizado

1. Copie `inputs/exemplo_apt304.json` para `inputs/seu_caso.json`
2. Edite os dados (cliente, caso, pendências)
3. Rode: `python gerar_pt_ad.py inputs/seu_caso.json`

## 📋 Estrutura do JSON de input

Veja o exemplo `inputs/exemplo_apt304.json` para a estrutura completa.

Campos obrigatórios:

- `documento`: tipo, sequencial, ano, data, revisão, status
- `cliente`: nome, cidade, destinatário
- `caso`: unidade, proprietário, ambiente, responsável técnico
- `objeto_finalidade`: textos descritivos
- `documentos_analisados`: lista de documentos
- `pendencias`: lista referenciando o catálogo (com overrides opcionais)
- `quadro_resumo`: tabela final consolidada
- `conclusao`: status, texto, encaminhamentos

## 🎨 Personalização

### Adicionar nova pendência reutilizável

Edite `pendencias.py` e adicione ao dicionário `PENDENCIAS_BASE`:

```python
"PD-NOVA": {
    "titulo": "Título da nova pendência",
    "constatacao": "...",
    "nao_conformidade": "...",
    "exigencia": "..."
}
```

Depois use no JSON: `{"codigo_base": "PD-NOVA", "numero": "PD-XX"}`.

### Ajustar cores ou fontes

Edite `estilos.py`. Cores estão no formato `RGBColor(R, G, B)`.

## 📚 Referência

- Especificação completa: `../TEMPLATE_DIAGNOSTIKA.md`
- Modelos analisados:
  - `Clientes/Primavera/Laudos e Pareceres/Parecer_Tecnico_Portal_Primavera_Bl07_Apt304.pdf`
  - `Clientes/Condomínio Edifício Menotti del Picchia/.../Parecer_Nao_Conformidades_Aditivo_AAM_Mai2026.pdf`

## 🛣️ Roadmap

- [x] **v0.1** — MVP PT-AD funcional
- [ ] **v0.2** — Conversão automática para PDF
- [ ] **v0.3** — Suporte a PT-NC (Não Conformidades)
- [ ] **v0.4** — Suporte a Laudo Técnico (com fotos integradas)
- [ ] **v0.5** — Integração com banco de demandas (catalogador WhatsApp)
- [ ] **v0.6** — Numeração sequencial automática (lê último DK-PT-AD-NNN existente)
- [ ] **v0.7** — Interface CLI amigável (sem precisar editar JSON manualmente)
- [ ] **v1.0** — Integração total: WhatsApp → catalogador → gerador → documento pronto
