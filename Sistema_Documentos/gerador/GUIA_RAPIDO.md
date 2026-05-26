# ⚡ GUIA RÁPIDO — Gerador Diagnóstika

> Cole este guia perto do PC. Comandos prontos para uso diário.

---

## 🔥 Comandos essenciais

### Gerar um parecer
```powershell
cd "C:\Users\rrcon\OneDrive\Área de Trabalho\Diagnóstika Engenharia\Admin Diagnostika\Sistema_Documentos\gerador"
$py = "C:\Users\rrcon\AppData\Local\Programs\Python\Python312\python.exe"
& $py gerar_pt_ad.py inputs/SEU_ARQUIVO.json
```

### Ver status do catálogo de normas
```powershell
& $py normas.py
```

### Listar pareceres gerados
```powershell
ls saidas
```

---

## 📝 Workflow padrão (10-15 min por parecer)

```
1. cd ...\gerador\inputs
2. Copy-Item exemplo_apt304.json caso_NOVO.json
3. Abre caso_NOVO.json no Bloco de Notas / VS Code
4. Edita: cliente, caso, pendências, conclusão
5. Salva
6. Volta pro PowerShell na pasta gerador
7. Roda: & $py gerar_pt_ad.py inputs/caso_NOVO.json
8. Abre o .docx em saidas/
9. Revisa no Word
10. Salva como PDF
```

---

## 🗂️ Campos essenciais do JSON

### Identificação do documento
```json
"documento": {
  "tipo": "PT-AD",
  "ref_sequencial": N,         ← incrementar a cada parecer do ano
  "ano": 2026,
  "data_emissao": "AAAA-MM-DD",
  "revisao": "Rev. 00 — Emissão inicial",
  "status_capa": "NÃO APROVADO"
}
```

### Cliente
```json
"cliente": {
  "nome_curto": "...",
  "nome_completo": "Condomínio ...",
  "cidade_uf": "Cidade/UF",
  "destinatario": "Administração do Condomínio ..."
}
```

### Caso
```json
"caso": {
  "tipo_solicitacao": "Solicitação de Reforma",
  "unidade": "Bloco XX — Apartamento YYY",
  "proprietario": "Nome do Proprietário",
  "ambiente": "Banheiro/Cozinha/Sala/...",
  "sistema_construtivo": "Alvenaria estrutural" ou "Convencional",
  "alvenaria_estrutural": true/false,
  "responsavel_tecnico": {
    "nome": "Eng. ...",
    "crea": "CREA-SP NNNNNNN",
    "art": "NNNNNNNN"
  },
  "servicos_declarados": "lista descritiva",
  "prazo_declarado": "X dias",
  "art_metragem": "X m²"
}
```

---

## 📋 Catálogo de pendências (PD)

| Código | Use quando... |
|---|---|
| `PD-IMPER` | reforma em área molhada, sem detalhar impermeabilização |
| `PD-ESTANQ` | falta teste de estanqueidade |
| `PD-CROQUI` | sem croqui/planta da área |
| `PD-ALVEN` | alvenaria estrutural sem declaração de não intervenção |
| `PD-ARTCMP` | ART e memorial divergem (m² ou escopo) |
| `PD-EXEC` | memorial sem detalhamento executivo |
| `PD-RUIDO` | sem plano de ruídos/horários |
| `PD-RESID` | sem plano de resíduos |

**Como usar no JSON:**
```json
"pendencias": [
  {"codigo_base": "PD-IMPER", "numero": "PD-01"},
  {"codigo_base": "PD-CROQUI", "numero": "PD-02"}
]
```

**Customizar texto:**
```json
{
  "codigo_base": "PD-ARTCMP",
  "numero": "PD-03",
  "override": {
    "constatacao": "texto específico deste caso..."
  }
}
```

---

## 📚 Normas no catálogo

| Status | Significado |
|---|---|
| `[OK]` | Vigente confirmada — pode usar tranquilo |
| `[??]` | Verificação pendente — confirmar na ABNT antes |
| `[!!]` | Potencialmente desatualizada — atualizar URGENTE |
| `[XX]` | Revogada — NÃO usar |

**Conferir antes de gerar:** `& $py normas.py`

**Para atualizar uma norma** depois de verificar:
1. Edita `normas_catalogo.json`
2. Muda `"status": "vigente_confirmada"`
3. Atualiza `"ultima_verificacao"` para hoje

---

## 🆘 Problemas comuns

### "Norma 'X' não está no catálogo registrado"
→ Adicionar a norma em `normas_catalogo.json` antes de usar

### "Pendência 'PD-XXX' não está no catálogo"
→ Adicionar a pendência em `pendencias.py` ou usar override de um código existente

### Documento gerado mas faltou algo
→ Verifique se o JSON tem todos os campos. Compare com `inputs/exemplo_apt304.json`

### Erro de encoding no console
→ Ignorar — o documento .docx é gerado mesmo assim

---

## 🎯 Status atual do sistema

- ✅ PT-AD (Parecer Técnico de Análise Documental)
- ⏳ PT-NC (Não Conformidades) — em planejamento
- ⏳ LT (Laudo Técnico) — em planejamento
- ⏳ Conversão automática PDF — em planejamento
- ⏳ Numeração automática — em planejamento

---

## 📞 Quando chamar o Claude

- "Monta o JSON pra mim, os dados são: ..."
- "Adicionar uma nova pendência ao catálogo"
- "Verificar e atualizar normas"
- "Implementar tipo X de documento"
- "Inserir fotos no documento"
- "Converter pra PDF automaticamente"

---

**Versão do guia:** 1.0
**Última atualização:** 26/05/2026
