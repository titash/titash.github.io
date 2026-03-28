"""MkDocs hook: regenerate resume.md and resume.pdf from resume.json on every build."""

import importlib.util
import os
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESUME_JSON = ROOT / "resume.json"
DOCS_PDF = ROOT / "docs" / "pdf" / "resume.pdf"

# Import generate() from scripts/generate_resume.py
_spec = importlib.util.spec_from_file_location(
    "generate_resume", ROOT / "scripts" / "generate_resume.py"
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
_generate = _mod.generate


def on_pre_build(config, **kwargs):
    """Regenerate resume.md and docs/pdf/resume.pdf from resume.json before each build."""
    if not RESUME_JSON.exists():
        return
    _generate()
    print("[resume_hook] Regenerated resume.md and resume.pdf from resume.json")


def on_post_build(config, **kwargs):
    """Copy the PDF into the built site directory."""
    if not DOCS_PDF.exists():
        return
    site_dir = config.get("site_dir", str(ROOT / "site"))
    dest = os.path.join(site_dir, "pdf", "resume.pdf")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    shutil.copy2(str(DOCS_PDF), dest)
