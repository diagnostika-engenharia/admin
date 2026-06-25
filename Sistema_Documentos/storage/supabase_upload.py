"""
Módulo de upload para Supabase Storage.

Usado pelos geradores de documentos (gerar_pt_ad.py etc.) para salvar
o documento gerado diretamente no Supabase Storage após a geração local.

Uso:
    from storage.supabase_upload import upload_documento

    local_path = gerar(...)
    result = upload_documento(local_path, condominio="Portal_Primavera", tipo="PT-AD")
    # result = {"storage_path": "Portal_Primavera/PT-AD/DK-PT-AD-001-2026.docx", ...}
"""

import mimetypes
import os
from datetime import datetime, timezone
from pathlib import Path

import httpx

SUPABASE_URL = os.environ.get("SUPABASE_URL", "https://fimmjgdwhifsrrbreche.supabase.co")
SUPABASE_KEY = os.environ.get("SUPABASE_SERVICE_KEY", "")
BUCKET = "documentos"


def upload_documento(local_path: Path, condominio: str, tipo: str,
                     extra_folder: str = "") -> dict:
    """
    Faz upload de um documento gerado para o Supabase Storage.

    Args:
        local_path: Caminho local do arquivo gerado (.docx, .pdf)
        condominio: Nome do condomínio (usado como pasta raiz no bucket)
        tipo: Tipo do documento (PT-AD, LT, RT, etc.)
        extra_folder: Subpasta adicional opcional

    Returns:
        dict com storage_path, url, size, ou error
    """
    if not SUPABASE_KEY:
        return {"ok": False, "error": "SUPABASE_SERVICE_KEY não configurada"}

    local_path = Path(local_path)
    if not local_path.exists():
        return {"ok": False, "error": f"Arquivo não encontrado: {local_path}"}

    parts = [condominio.replace(" ", "_"), tipo]
    if extra_folder:
        parts.append(extra_folder.replace(" ", "_"))
    parts.append(local_path.name.replace(" ", "_"))
    storage_path = "/".join(parts)

    mime = mimetypes.guess_type(str(local_path))[0] or "application/octet-stream"
    size = local_path.stat().st_size

    with open(local_path, "rb") as f:
        resp = httpx.post(
            f"{SUPABASE_URL}/storage/v1/object/{BUCKET}/{storage_path}",
            headers={
                "apikey": SUPABASE_KEY,
                "Authorization": f"Bearer {SUPABASE_KEY}",
                "Content-Type": mime,
                "x-upsert": "true",
            },
            content=f.read(),
            timeout=120,
        )

    if resp.status_code not in (200, 201):
        return {"ok": False, "error": resp.text, "status": resp.status_code}

    return {
        "ok": True,
        "storage_path": storage_path,
        "size": size,
        "mime": mime,
        "uploaded_at": datetime.now(timezone.utc).isoformat(),
    }


def registrar_no_catalogo(storage_path: str, size: int, mime: str,
                          metadata: dict = None) -> bool:
    """
    Insere ou atualiza o registro no catalogo_documentos.
    metadata pode conter: titulo, condominio, tipo_documento, etc.
    """
    if not SUPABASE_KEY:
        return False

    payload = {
        "storage_path": storage_path,
        "file_size_bytes": size,
        "mime_type": mime,
        "uploaded_at": datetime.now(timezone.utc).isoformat(),
    }
    if metadata:
        payload.update(metadata)

    resp = httpx.post(
        f"{SUPABASE_URL}/rest/v1/catalogo_documentos",
        headers={
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json",
            "Prefer": "resolution=merge-duplicates,return=minimal",
        },
        json=payload,
        timeout=30,
    )
    return resp.status_code in (200, 201)


def gerar_url_assinada(storage_path: str, expiry_seconds: int = 3600) -> str | None:
    """Gera URL assinada para download temporário (usada pelo n8n)."""
    if not SUPABASE_KEY:
        return None

    resp = httpx.post(
        f"{SUPABASE_URL}/storage/v1/object/sign/{BUCKET}/{storage_path}",
        headers={
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json",
        },
        json={"expiresIn": expiry_seconds},
        timeout=30,
    )

    if resp.status_code == 200:
        data = resp.json()
        return f"{SUPABASE_URL}/storage/v1{data['signedURL']}"
    return None
