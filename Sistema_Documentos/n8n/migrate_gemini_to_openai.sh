#!/usr/bin/env bash
# ============================================================
# migrate_gemini_to_openai.sh
# Substitui todos os nós Gemini por OpenAI GPT-4o-mini
# no workflow do Robô IA (qeJQVvrn9X7MDnjK)
#
# Rodar NA VPS (84.46.248.23):
#   chmod +x migrate_gemini_to_openai.sh
#   ./migrate_gemini_to_openai.sh
#
# Pré-requisitos:
#   - jq instalado (apt install jq)
#   - N8N_API_KEY definida OU editar a variável abaixo
# ============================================================

set -euo pipefail

N8N_BASE="http://localhost:5678"
WORKFLOW_ID="qeJQVvrn9X7MDnjK"
OPENAI_CRED_ID="oxUNjZdVarEJYg3x"
OPENAI_CRED_NAME="OpenAI - Diagnóstika"
MODEL="gpt-4o-mini"

# API key do n8n — pegar em Settings > API > API Keys
N8N_API_KEY="${N8N_API_KEY:-}"

if [ -z "$N8N_API_KEY" ]; then
    echo "[ERRO] Defina N8N_API_KEY no ambiente ou edite este script."
    echo "       Pegue em: n8n > Settings > API > Create API Key"
    exit 1
fi

AUTH_HEADER="X-N8N-API-KEY: $N8N_API_KEY"

echo "=== Etapa 1: Backup do workflow atual ==="
BACKUP_FILE="workflow_backup_$(date +%Y%m%d_%H%M%S).json"
curl -sS "$N8N_BASE/api/v1/workflows/$WORKFLOW_ID" \
    -H "$AUTH_HEADER" \
    -H "Accept: application/json" \
    > "$BACKUP_FILE"

NODE_COUNT=$(jq '.nodes | length' "$BACKUP_FILE")
echo "    Workflow baixado: $NODE_COUNT nós. Backup: $BACKUP_FILE"

echo ""
echo "=== Etapa 2: Identificar nós Gemini ==="
GEMINI_NODES=$(jq -r '.nodes[] | select(
    .type == "@n8n/n8n-nodes-langchain.lmChatGoogleGemini" or
    .type == "n8n-nodes-base.googleGemini" or
    .type == "@n8n/n8n-nodes-langchain.lmChatGoogleVertex" or
    (.type | test("gemini|google.*chat"; "i"))
) | .name' "$BACKUP_FILE")

if [ -z "$GEMINI_NODES" ]; then
    echo "    Nenhum nó Gemini encontrado com tipos padrão."
    echo "    Listando todos os tipos de nó para verificação manual:"
    jq -r '.nodes[] | "\(.name) → \(.type)"' "$BACKUP_FILE" | grep -iE "gemini|google|lm|chat|ai|lang" || echo "    (nenhum match)"
    echo ""
    echo "    Verifique o backup e ajuste o script se necessário."
    exit 0
fi

echo "    Nós Gemini encontrados:"
echo "$GEMINI_NODES" | while read -r name; do
    echo "      - $name"
done

echo ""
echo "=== Etapa 3: Substituir nós Gemini por OpenAI ==="

# Função jq que transforma cada nó Gemini em OpenAI Chat Model
TRANSFORM=$(cat <<'JQEOF'
.nodes = [.nodes[] |
    if (
        .type == "@n8n/n8n-nodes-langchain.lmChatGoogleGemini" or
        .type == "n8n-nodes-base.googleGemini" or
        .type == "@n8n/n8n-nodes-langchain.lmChatGoogleVertex" or
        (.type | test("gemini|google.*chat"; "i"))
    ) then
        # Preservar: name, position, connections (ficam no nível do workflow)
        # Trocar: type, typeVersion, credentials, parameters
        .type = "@n8n/n8n-nodes-langchain.lmChatOpenAi" |
        .typeVersion = 1.2 |
        .credentials = {
            "openAiApi": {
                "id": $cred_id,
                "name": $cred_name
            }
        } |
        # Preservar system prompt se existir nos parameters
        .parameters = (
            (.parameters // {}) |
            {
                "model": $model,
                "options": {
                    "temperature": (.options.temperature // 0.3),
                    "maxTokens": (.options.maxTokens // .options.maxOutputTokens // 4096),
                    "responseFormat": (.options.responseFormat // "text")
                }
            } + (if .systemMessage then {"systemMessage": .systemMessage} else {} end)
              + (if .messages then {"messages": .messages} else {} end)
        )
    else
        .
    end
]
JQEOF
)

UPDATED_FILE="workflow_updated.json"
jq --arg cred_id "$OPENAI_CRED_ID" \
   --arg cred_name "$OPENAI_CRED_NAME" \
   --arg model "$MODEL" \
   "$TRANSFORM" "$BACKUP_FILE" > "$UPDATED_FILE"

GEMINI_AFTER=$(jq '[.nodes[] | select(.type | test("gemini|google.*chat"; "i"))] | length' "$UPDATED_FILE")
OPENAI_COUNT=$(jq '[.nodes[] | select(.type | test("openAi"; "i"))] | length' "$UPDATED_FILE")

echo "    Nós Gemini restantes: $GEMINI_AFTER (deve ser 0)"
echo "    Nós OpenAI total: $OPENAI_COUNT"

if [ "$GEMINI_AFTER" -ne 0 ]; then
    echo "[AVISO] Ainda há nós Gemini. Verifique manualmente."
fi

echo ""
echo "=== Etapa 4: Enviar workflow atualizado ==="
RESPONSE=$(curl -sS -X PUT "$N8N_BASE/api/v1/workflows/$WORKFLOW_ID" \
    -H "$AUTH_HEADER" \
    -H "Content-Type: application/json" \
    -d @"$UPDATED_FILE")

UPDATED_AT=$(echo "$RESPONSE" | jq -r '.updatedAt // "erro"')

if [ "$UPDATED_AT" != "erro" ] && [ "$UPDATED_AT" != "null" ]; then
    echo "    Workflow atualizado com sucesso! (updatedAt: $UPDATED_AT)"
else
    echo "[ERRO] Falha ao atualizar:"
    echo "$RESPONSE" | jq '.' 2>/dev/null || echo "$RESPONSE"
    echo ""
    echo "Workflow modificado salvo em: $UPDATED_FILE"
    echo "Você pode importar manualmente pelo dashboard do n8n."
    exit 1
fi

echo ""
echo "=== Etapa 5: Ativar workflow ==="
curl -sS -X PATCH "$N8N_BASE/api/v1/workflows/$WORKFLOW_ID" \
    -H "$AUTH_HEADER" \
    -H "Content-Type: application/json" \
    -d '{"active": true}' > /dev/null

echo "    Workflow ativado."
echo ""
echo "=== Concluído ==="
echo "Backup: $BACKUP_FILE"
echo "Para reverter: curl -X PUT $N8N_BASE/api/v1/workflows/$WORKFLOW_ID -H 'X-N8N-API-KEY: ...' -H 'Content-Type: application/json' -d @$BACKUP_FILE"
echo ""
echo "PRÓXIMO PASSO: teste enviando uma mensagem no grupo WhatsApp e verifique"
echo "se a classificação retorna o JSON correto (demanda/info/urgência/etc)."
