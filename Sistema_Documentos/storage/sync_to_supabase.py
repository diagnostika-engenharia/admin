"""
Sync de documentos locais para Supabase Storage.

Uso:
    # Sync completo (todos os arquivos da pasta de clientes)
    python sync_to_supabase.py --full

    # Sync de um arquivo específico
    python sync_to_supabase.py --file "caminho/do/arquivo.pdf"

    # Dry-run (lista o que seria enviado, sem enviar)
    python sync_to_supabase.py --full --dry-run

Variáveis de ambiente necessárias:
    SUPABASE_URL       - URL do projeto Supabase
    SUPABASE_SERVICE_KEY - Service role key (não anon key)
    DOCS_ROOT_LOCAL    - Raiz local dos documentos (default: OneDrive do Rogério)
"""

import argparse
import mimetypes
import os
import sys
import time
from pathlib import Path

import httpx

SUPABASE_URL = os.environ.get("SUPABASE_URL", "https://fimmjgdwhifsrrbreche.supabase.co")
SUPABASE_KEY = os.environ.get("SUPABASE_SERVICE_KEY", "")
BUCKET = "documentos"

DEFAULT_DOCS_ROOT = Path(
    r"C:\Users\rrcon\OneDrive\Área de Trabalho\Diagnóstika Engenharia\Clientes"
)

EXTENSIONS = {".pdf", ".docx", ".xlsx", ".xls", ".jpg", ".jpeg", ".png", ".doc"}


def headers():
    return {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
    }


def storage_path_from_local(file_path: Path, root: Path) -> str:
    """Converte caminho local em path do bucket (sem caracteres problemáticos)."""
    rel = file_path.relative_to(root)
    parts = [p.replace(" ", "_") for p in rel.parts]
    return "/".join(parts)


def upload_file(client: httpx.Client, file_path: Path, storage_path: str) -> dict:
    """Upload de um arquivo para o Supabase Storage."""
    mime = mimetypes.guess_type(str(file_path))[0] or "application/octet-stream"
    size = file_path.stat().st_size

    with open(file_path, "rb") as f:
        resp = client.post(
            f"{SUPABASE_URL}/storage/v1/object/{BUCKET}/{storage_path}",
            headers={
                **headers(),
                "Content-Type": mime,
                "x-upsert": "true",
            },
            content=f.read(),
            timeout=120,
        )

    if resp.status_code not in (200, 201):
        return {"ok": False, "error": resp.text, "storage_path": storage_path}

    return {
        "ok": True,
        "storage_path": storage_path,
        "size": size,
        "mime": mime,
    }


def update_catalogo(client: httpx.Client, storage_path: str, size: int, mime: str,
                    caminho_local: str):
    """Atualiza catalogo_documentos com o storage_path do arquivo enviado."""
    resp = client.patch(
        f"{SUPABASE_URL}/rest/v1/catalogo_documentos",
        headers={
            **headers(),
            "Content-Type": "application/json",
            "Prefer": "return=minimal",
        },
        params={"caminho_local": f"eq.{caminho_local}"},
        json={
            "storage_path": storage_path,
            "file_size_bytes": size,
            "mime_type": mime,
            "uploaded_at": "now()",
        },
    )
    return resp.status_code in (200, 204)


def collect_files(root: Path) -> list[Path]:
    """Lista todos os arquivos elegíveis recursivamente."""
    files = []
    for ext in EXTENSIONS:
        files.extend(root.rglob(f"*{ext}"))
        files.extend(root.rglob(f"*{ext.upper()}"))
    return sorted(set(files))


def get_already_uploaded(client: httpx.Client) -> set[str]:
    """Busca storage_paths já presentes no catálogo."""
    resp = client.get(
        f"{SUPABASE_URL}/rest/v1/catalogo_documentos",
        headers={**headers(), "Content-Type": "application/json"},
        params={"select": "storage_path", "storage_path": "not.is.null"},
    )
    if resp.status_code == 200:
        return {r["storage_path"] for r in resp.json()}
    return set()


def main():
    parser = argparse.ArgumentParser(description="Sync documentos para Supabase Storage")
    parser.add_argument("--full", action="store_true", help="Sync completo da pasta raiz")
    parser.add_argument("--file", type=str, help="Caminho de um arquivo específico")
    parser.add_argument("--dry-run", action="store_true", help="Listar sem enviar")
    parser.add_argument("--root", type=str, default=str(DEFAULT_DOCS_ROOT),
                        help="Pasta raiz dos documentos")
    args = parser.parse_args()

    if not SUPABASE_KEY:
        print("[ERRO] Defina SUPABASE_SERVICE_KEY no ambiente.")
        sys.exit(1)

    root = Path(args.root)

    if args.file:
        files = [Path(args.file)]
    elif args.full:
        if not root.exists():
            print(f"[ERRO] Pasta raiz não encontrada: {root}")
            sys.exit(1)
        files = collect_files(root)
    else:
        parser.print_help()
        sys.exit(0)

    print(f"Encontrados {len(files)} arquivos para sync.")

    total_size = sum(f.stat().st_size for f in files if f.exists())
    print(f"Tamanho total: {total_size / (1024*1024):.1f} MB")

    if total_size > 1_000_000_000:
        print(f"[AVISO] Total > 1GB ({total_size/(1024*1024*1024):.2f} GB).")
        print("        Supabase free tier = 1GB. Considere o plano Pro ou priorizar.")

    if args.dry_run:
        for f in files[:20]:
            sp = storage_path_from_local(f, root) if args.full else f.name
            print(f"  {sp} ({f.stat().st_size/1024:.0f} KB)")
        if len(files) > 20:
            print(f"  ... e mais {len(files) - 20} arquivos")
        return

    client = httpx.Client()
    already = get_already_uploaded(client)
    print(f"Já enviados: {len(already)}")

    ok_count = 0
    err_count = 0

    for i, f in enumerate(files, 1):
        if not f.exists():
            continue

        sp = storage_path_from_local(f, root) if args.full else f.name
        if sp in already:
            continue

        result = upload_file(client, f, sp)
        if result["ok"]:
            ok_count += 1
            caminho_local = str(f)
            update_catalogo(client, sp, result["size"], result["mime"], caminho_local)
            if i % 50 == 0:
                print(f"  [{i}/{len(files)}] {ok_count} OK, {err_count} erros")
        else:
            err_count += 1
            print(f"  [ERRO] {sp}: {result['error'][:100]}")

        if i % 100 == 0:
            time.sleep(1)

    print(f"\nConcluído: {ok_count} enviados, {err_count} erros, {len(already)} já existiam.")
    client.close()


if __name__ == "__main__":
    main()
