"""MkDocs hook: regenerate resume PDF from docs/resume.md on every build."""

import os
import re
from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parent.parent
RESUME_MD = ROOT / "docs" / "resume.md"

# Theme colors (matching jabid.in blog style)
COLOR_TEXT = HexColor("#222222")
COLOR_TITLE = HexColor("#222222")
COLOR_H2 = HexColor("#393939")
COLOR_H3 = HexColor("#494949")
COLOR_LINK = HexColor("#3399cc")
COLOR_BG = HexColor("#ffffff")

# Register fonts
FONT = "DejaVuSans"
FONT_BOLD = "DejaVuSans-Bold"
try:
    pdfmetrics.registerFont(TTFont(FONT, "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
    pdfmetrics.registerFont(TTFont(FONT_BOLD, "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
except Exception:
    FONT = "Helvetica"
    FONT_BOLD = "Helvetica-Bold"


def _parse_resume_md(text):
    """Parse resume.md into structured sections for PDF rendering."""
    sections = []
    current_section = None
    current_lines = []

    for line in text.splitlines():
        if line.startswith("# ") and not line.startswith("## "):
            # Top-level heading = name
            sections.append(("_name", [line[2:].strip()]))
        elif line.startswith("## "):
            if current_section is not None:
                sections.append((current_section, current_lines))
            current_section = line[3:].strip()
            current_lines = []
        else:
            current_lines.append(line)

    if current_section is not None:
        sections.append((current_section, current_lines))

    return sections


def _generate_pdf(output_path, sections):
    """Render PDF from parsed sections using reportlab."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    c = canvas.Canvas(str(output_path), pagesize=letter)
    w, h = letter
    left = 0.6 * inch
    right = w - 0.6 * inch
    max_text = right - left
    top = h - 0.6 * inch
    bottom = 0.5 * inch

    y = top

    # Background
    c.setFillColor(COLOR_BG)
    c.rect(0, 0, w, h, fill=1, stroke=0)

    def new_page():
        nonlocal y
        c.showPage()
        c.setFillColor(COLOR_BG)
        c.rect(0, 0, w, h, fill=1, stroke=0)
        y = top

    def draw_text(s, font=FONT, size=9, spacing=12, color=COLOR_TEXT, indent=0):
        nonlocal y
        if not s.strip():
            return
        c.setFillColor(color)
        c.setFont(font, size)
        avail = max_text - indent
        words = s.split()
        line = ""
        for word in words:
            test = f"{line} {word}".strip()
            if c.stringWidth(test, font, size) > avail:
                if y < bottom:
                    new_page()
                    c.setFillColor(color)
                    c.setFont(font, size)
                c.drawString(left + indent, y, line)
                y -= spacing
                line = word
            else:
                line = test
        if line:
            if y < bottom:
                new_page()
                c.setFillColor(color)
                c.setFont(font, size)
            c.drawString(left + indent, y, line)
            y -= spacing

    def draw_section_header(title):
        nonlocal y
        y -= 6
        c.setStrokeColor(HexColor("#e5e5e5"))
        c.setLineWidth(0.6)
        c.line(left, y + 10, right, y + 10)
        y -= 2
        draw_text(title, FONT_BOLD, 10.5, 14, COLOR_H2)

    # --- Pass 1: measure total content height for spacing --- #
    def measure_text(s, font, size, spacing, indent=0):
        avail = max_text - indent
        words = s.split()
        lines = 1
        line = ""
        for word in words:
            test = f"{line} {word}".strip()
            if c.stringWidth(test, font, size) > avail:
                lines += 1
                line = word
            else:
                line = test
        return lines * spacing

    total_h = 0
    section_count = 0
    for name, lines in sections:
        if name == "_name":
            total_h += 19 + 13 + 14  # name + subtitle + contact
            continue
        if name == "Download as PDF":
            continue
        section_count += 1
        total_h += 16  # section header
        for line in lines:
            line = line.strip()
            if not line:
                continue
            # Strip markdown formatting for measurement
            plain = re.sub(r'\*\*(.+?)\*\*', r'\1', line)
            plain = re.sub(r'\*(.+?)\*', r'\1', plain)
            plain = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', plain)
            if line.startswith("### "):
                total_h += 12
            elif line.startswith("- "):
                total_h += measure_text(f"\u2022  {plain[2:]}", FONT, 8.5, 11, indent=8)
            else:
                total_h += measure_text(plain, FONT, 9, 12)

    usable = top - bottom
    remaining = usable - total_h
    extra_gap = max(remaining / max(section_count, 1), 0)
    extra_gap = min(extra_gap, 18)

    # --- Pass 2: render --- #
    name_info = next((lines for name, lines in sections if name == "_name"), None)
    header_lines_after_name = []

    for sec_name, lines in sections:
        if sec_name == "_name":
            draw_text(lines[0], FONT_BOLD, 17, 19, COLOR_TITLE)
            # Next section's first lines before ## are subtitle/contact
            continue

        if sec_name == "Download as PDF":
            continue

        # Collect non-empty content lines
        content = [l for l in lines]

        # Check if this is the first section — its leading lines before content
        # are the subtitle + contact info that come right after # Name
        if sec_name == sections[1][0] if len(sections) > 1 else False:
            pass

        # Find subtitle and contact lines (between # name and first ##)
        # These are already in the first section's lines

        draw_section_header(sec_name)
        y -= extra_gap - 6  # apply distributed spacing

        for line in content:
            stripped = line.strip()
            if not stripped:
                continue

            # Strip markdown links: [text](url) → text
            plain = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', stripped)

            if stripped.startswith("### "):
                title = re.sub(r'\*\*(.+?)\*\*', r'\1', plain[4:])
                title = re.sub(r'\*(.+?)\*', r'\1', title)
                draw_text(title, FONT_BOLD, 8.5, 12, COLOR_TITLE)
            elif stripped.startswith("- "):
                bullet_text = re.sub(r'\*\*(.+?)\*\*', r'\1', plain[2:])
                draw_text(f"\u2022  {bullet_text}", FONT, 8.5, 11, COLOR_TEXT, indent=8)
            elif stripped.startswith("**") and stripped.endswith("**"):
                bold_text = stripped.strip("*")
                draw_text(bold_text, FONT_BOLD, 9, 12, COLOR_TEXT)
            elif stripped.startswith("**"):
                # Bold prefix line like **Title**: content
                rendered = re.sub(r'\*\*(.+?)\*\*', r'\1', plain)
                draw_text(rendered, FONT, 8.5, 11, COLOR_TEXT)
            elif stripped.startswith("*") and stripped.endswith("*"):
                italic_text = stripped.strip("*")
                draw_text(italic_text, FONT, 8, 11, COLOR_H3)
            else:
                draw_text(plain, FONT, 9, 12, COLOR_TEXT)

    c.save()


def _render_header(sections):
    """Extract header info (subtitle + contact) from raw lines between name and first section."""
    for name, lines in sections:
        if name == "_name":
            continue
        if name == "Download as PDF":
            continue
        # The first real section — check if there are header lines
        # Actually the subtitle/contact are before the first ## in the raw file
        # They end up in a pseudo-section. Let me handle differently.
        break


def on_post_build(config, **kwargs):
    """MkDocs hook: regenerate PDF after each build."""
    if not RESUME_MD.exists():
        return

    md_text = RESUME_MD.read_text()
    sections = _parse_resume_md(md_text)

    # Handle subtitle + contact lines that come right after # Name
    # They appear as lines before the first ## section, so they're part
    # of the _name pseudo-section or loose lines. Let's fix the parser
    # to capture them properly.

    # Re-parse to extract header lines (between # Name and first ##)
    header_lines = []
    found_name = False
    for line in md_text.splitlines():
        if line.startswith("# ") and not line.startswith("## "):
            found_name = True
            continue
        if found_name and line.startswith("## "):
            break
        if found_name and line.strip():
            header_lines.append(line.strip())

    site_dir = config.get("site_dir", str(ROOT / "site"))
    output_path = os.path.join(site_dir, "pdf", "resume.pdf")

    # Also write to docs/pdf for source tracking
    docs_pdf = str(ROOT / "docs" / "pdf" / "resume.pdf")

    # Build a modified sections list that includes header rendering
    _generate_pdf_with_header(output_path, sections, header_lines)
    # Copy to docs/pdf too
    os.makedirs(os.path.dirname(docs_pdf), exist_ok=True)
    import shutil
    shutil.copy2(output_path, docs_pdf)

    print(f"[pdf_hook] Regenerated {output_path}")


def _generate_pdf_with_header(output_path, sections, header_lines):
    """Full PDF generation with header info."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    c = canvas.Canvas(str(output_path), pagesize=letter)
    w, h = letter
    left = 0.6 * inch
    right = w - 0.6 * inch
    max_text = right - left
    top = h - 0.6 * inch
    bottom = 0.5 * inch

    y = top

    c.setFillColor(COLOR_BG)
    c.rect(0, 0, w, h, fill=1, stroke=0)

    def new_page():
        nonlocal y
        c.showPage()
        c.setFillColor(COLOR_BG)
        c.rect(0, 0, w, h, fill=1, stroke=0)
        y = top

    def draw_text(s, font=FONT, size=9, spacing=12, color=COLOR_TEXT, indent=0):
        nonlocal y
        if not s.strip():
            return
        c.setFillColor(color)
        c.setFont(font, size)
        avail = max_text - indent
        words = s.split()
        line = ""
        for word in words:
            test = f"{line} {word}".strip()
            if c.stringWidth(test, font, size) > avail:
                if y < bottom:
                    new_page()
                    c.setFillColor(color)
                    c.setFont(font, size)
                c.drawString(left + indent, y, line)
                y -= spacing
                line = word
            else:
                line = test
        if line:
            if y < bottom:
                new_page()
                c.setFillColor(color)
                c.setFont(font, size)
            c.drawString(left + indent, y, line)
            y -= spacing

    def measure_text(s, font, size, spacing, indent=0):
        avail = max_text - indent
        words = s.split()
        lines = 1
        line = ""
        for word in words:
            test = f"{line} {word}".strip()
            if c.stringWidth(test, font, size) > avail:
                lines += 1
                line = word
            else:
                line = test
        return lines * spacing

    # --- Measure for spacing --- #
    total_h = 19 + len(header_lines) * 13  # name + header lines
    section_count = 0
    for sec_name, lines in sections:
        if sec_name == "_name" or sec_name == "Download as PDF":
            continue
        section_count += 1
        total_h += 16
        for line in lines:
            stripped = line.strip()
            if not stripped:
                continue
            plain = re.sub(r'\*\*(.+?)\*\*', r'\1', stripped)
            plain = re.sub(r'\*(.+?)\*', r'\1', plain)
            plain = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', plain)
            if stripped.startswith("### "):
                total_h += 12
            elif stripped.startswith("- "):
                total_h += measure_text(f"\u2022  {plain[2:]}", FONT, 8.5, 11, indent=8)
            else:
                total_h += measure_text(plain, FONT, 9, 12)

    usable = top - bottom
    remaining = usable - total_h
    extra_gap = max(remaining / max(section_count, 1), 0)
    extra_gap = min(extra_gap, 18)

    # --- Render --- #
    # Name
    name_text = None
    for sec_name, lines in sections:
        if sec_name == "_name":
            name_text = lines[0]
            break
    if name_text:
        draw_text(name_text, FONT_BOLD, 17, 19, COLOR_TITLE)

    # Header lines (subtitle, contact)
    for hl in header_lines:
        plain = re.sub(r'\*\*(.+?)\*\*', r'\1', hl)
        if hl.startswith("**"):
            draw_text(plain, FONT, 9, 13, COLOR_H3)
        else:
            draw_text(plain, FONT, 9, 14, COLOR_TEXT)

    # Sections
    for sec_name, lines in sections:
        if sec_name == "_name" or sec_name == "Download as PDF":
            continue

        y -= extra_gap
        c.setStrokeColor(HexColor("#e5e5e5"))
        c.setLineWidth(0.6)
        c.line(left, y + 10, right, y + 10)
        y -= 2
        draw_text(sec_name, FONT_BOLD, 10.5, 14, COLOR_H2)

        for line in lines:
            stripped = line.strip()
            if not stripped:
                continue

            plain = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', stripped)

            if stripped.startswith("### "):
                title = re.sub(r'\*\*(.+?)\*\*', r'\1', plain[4:])
                title = re.sub(r'\*(.+?)\*', r'\1', title)
                draw_text(title, FONT_BOLD, 8.5, 12, COLOR_TITLE)
            elif stripped.startswith("- "):
                bullet_text = re.sub(r'\*\*(.+?)\*\*', r'\1', plain[2:])
                draw_text(f"\u2022  {bullet_text}", FONT, 8.5, 11, COLOR_TEXT, indent=8)
            elif stripped.startswith("**") and stripped.endswith("**"):
                draw_text(stripped.strip("*"), FONT_BOLD, 9, 12, COLOR_TEXT)
            elif stripped.startswith("**"):
                rendered = re.sub(r'\*\*(.+?)\*\*', r'\1', plain)
                draw_text(rendered, FONT, 8.5, 11, COLOR_TEXT)
            elif stripped.startswith("*") and stripped.endswith("*"):
                draw_text(stripped.strip("*"), FONT, 8, 11, COLOR_H3)
            else:
                draw_text(plain, FONT, 9, 12, COLOR_TEXT)

    c.save()
