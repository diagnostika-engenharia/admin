# Supabase Storage — Documentos Diagnóstika

## Decisão: Opção A (Supabase Storage)

**Por quê:**
- Supabase já é a base de tudo (auth, banco, RLS) — sem nova dependência
- n8n já tem credencial Supabase configurada — acesso direto via REST
- Sem risco de conta pessoal Microsoft (Graph API com conta pessoal tem limitações de app registration)
- Latência menor: Storage na mesma infra do banco vs chamadas à API Microsoft
- Documentos gerados pelo sistema salvam direto no bucket, sem intermediário

**Trade-off:** se os 1.624 docs passarem de 1GB, precisa do plano Pro ($25/mês ≈ R$125/mês) ou priorizar os mais pedidos.

---

## Setup (passo a passo)

### 1. Rodar migration no Supabase

No SQL Editor do dashboard Supabase (`fimmjgdwhifsrrbreche`):
- Copiar e executar `migration_storage.sql`
- Isso cria o bucket `documentos`, adiciona colunas à tabela, cria a view e função RPC

### 2. Sync inicial (no PC do Rogério)

```bash
pip install httpx
set SUPABASE_SERVICE_KEY=<service_role_key_do_dashboard>
python sync_to_supabase.py --full --dry-run   # ver tamanho total primeiro
python sync_to_supabase.py --full              # subir tudo
```

### 3. Configurar n8n (VPS)

No workflow do Robô IA, após o nó que busca no `catalogo_documentos`:

**Nó HTTP Request — Baixar arquivo do Storage:**
```
Method: POST
URL: https://fimmjgdwhifsrrbreche.supabase.co/storage/v1/object/sign/documentos/{{$json.storage_path}}
Headers:
  apikey: {{$credentials.supabaseApi.apiKey}}
  Authorization: Bearer {{$credentials.supabaseApi.apiKey}}
  Content-Type: application/json
Body: {"expiresIn": 3600}
```

Isso retorna uma `signedURL`. Use-a para baixar o arquivo e enviar via MegaZap.

**Nó HTTP Request — Enviar via MegaZap:**
```
URL da API MegaZap v2 para envio de arquivo
Body: { "url": "<signedURL do passo anterior>" }
```

### 4. Variáveis de ambiente na VPS

Adicionar ao `.env` do n8n ou do container Docker:
```
SUPABASE_SERVICE_KEY=eyJ...  (service_role key, NÃO a anon key)
```

---

## Estrutura do bucket

```
documentos/
├── Portal_Primavera/
│   ├── PT-AD/
│   │   └── DK-PT-AD-001-2026_Portal_Primavera.docx
│   ├── Laudos/
│   └── Aprovacoes/
├── Monte_Carlo/
│   ├── PT-AD/
│   └── ...
└── Morada_Morumbi/
    └── ...
```

---

## Estimativa de custos

| Cenário | Storage | Plano | Custo mensal |
|---------|---------|-------|-------------|
| < 1GB | Free tier | Free | R$ 0 |
| 1-5GB | Pro | Pro | ~R$ 125 |
| 5-50GB | Pro | Pro | ~R$ 125 (inclui 100GB) |

Os documentos são majoritariamente .docx (50-200KB cada) e PDFs (100KB-5MB).
Estimativa para 1.624 docs: **~300MB a 1.5GB** dependendo dos PDFs com imagens.
