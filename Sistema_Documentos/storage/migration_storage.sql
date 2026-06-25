-- ============================================================
-- Migration: Supabase Storage para Documentos Diagnóstika
-- Execução: rodar no SQL Editor do Supabase Dashboard
-- ============================================================

-- 1. Criar bucket para documentos
INSERT INTO storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
VALUES (
    'documentos',
    'documentos',
    false,
    52428800,  -- 50MB por arquivo
    ARRAY[
        'application/pdf',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        'application/vnd.ms-excel',
        'image/jpeg',
        'image/png',
        'application/octet-stream'
    ]
)
ON CONFLICT (id) DO NOTHING;

-- 2. Adicionar colunas de storage ao catalogo_documentos
ALTER TABLE catalogo_documentos
    ADD COLUMN IF NOT EXISTS storage_path TEXT,
    ADD COLUMN IF NOT EXISTS storage_url TEXT,
    ADD COLUMN IF NOT EXISTS uploaded_at TIMESTAMPTZ,
    ADD COLUMN IF NOT EXISTS file_size_bytes BIGINT,
    ADD COLUMN IF NOT EXISTS mime_type TEXT;

-- 3. Índice para busca rápida por storage_path
CREATE INDEX IF NOT EXISTS idx_catalogo_docs_storage_path
    ON catalogo_documentos (storage_path)
    WHERE storage_path IS NOT NULL;

-- 4. Índice para documentos ainda não sincronizados
CREATE INDEX IF NOT EXISTS idx_catalogo_docs_not_uploaded
    ON catalogo_documentos (id)
    WHERE storage_path IS NULL;

-- 5. RLS: service_role tem acesso total ao bucket
CREATE POLICY "Service role full access"
    ON storage.objects FOR ALL
    USING (bucket_id = 'documentos')
    WITH CHECK (bucket_id = 'documentos');

-- 6. View auxiliar para o n8n buscar documentos com URL assinada
CREATE OR REPLACE VIEW v_catalogo_com_storage AS
SELECT
    cd.*,
    CASE
        WHEN cd.storage_path IS NOT NULL THEN true
        ELSE false
    END AS disponivel_na_nuvem
FROM catalogo_documentos cd;

-- 7. Função para gerar URL assinada (usada pelo n8n via RPC)
CREATE OR REPLACE FUNCTION gerar_url_documento(p_storage_path TEXT, p_expiry_seconds INT DEFAULT 3600)
RETURNS TEXT
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
DECLARE
    v_url TEXT;
BEGIN
    SELECT
        (storage.fns.get_signed_url('documentos', p_storage_path, p_expiry_seconds)).signed_url
    INTO v_url;

    RETURN v_url;
END;
$$;
