"""Generate docs/resume.md and docs/pdf/resume.pdf from resume.json."""

import json
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parent.parent
RESUME_JSON = ROOT / "resume.json"
RESUME_MD = ROOT / "docs" / "resume.md"
PDF_PATH = ROOT / "docs" / "pdf" / "resume.pdf"

# Theme colors (matching jabid.in blog style)
COLOR_TEXT = HexColor("#222222")
COLOR_TITLE = HexColor("#222222")
COLOR_H2 = HexColor("#393939")
COLOR_H3 = HexColor("#494949")
COLOR_LINK = HexColor("#3399cc")
COLOR_BG = HexColor("#ffffff")

# Register DejaVu Sans (matches theme's system-ui sans-serif stack)
FONT = "DejaVuSans"
FONT_BOLD = "DejaVuSans-Bold"
pdfmetrics.registerFont(TTFont(FONT, "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont(FONT_BOLD, "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))


def generate_pdf(data):
    """Render a well-spaced one-page resume PDF with theme-matching styles."""
    PDF_PATH.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(PDF_PATH), pagesize=letter)
    w, h = letter
    left = 0.6 * inch
    right = w - 0.6 * inch
    max_text = right - left
    top = h - 0.6 * inch
    bottom = 0.5 * inch
    usable = top - bottom

    # --- Pass 1: measure total content height --- #
    def measure_text(s, font, size, spacing, indent=0):
        """Return height consumed by wrapped text."""
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

    # Count sections and measure content
    sections = []  # list of (title, content_height)

    # Header block (name + subtitle + contact)
    header_h = 19 + 13 + 14
    summary_h = measure_text(data["summary"], FONT, 9, 12)
    sections.append(("Summary", summary_h))

    skills_h = sum(
        measure_text(
            f"{''.join(f' {ch}' if ch.isupper() else ch for ch in cat).strip().title()}: {', '.join(skills)}",
            FONT, 8.5, 11,
        )
        for cat, skills in data["skills"].items()
    )
    sections.append(("Skills", skills_h))

    exp_h = 0
    for job in data["experience"]:
        exp_h += 12  # job title line
        for hl in job["highlights"][:3]:
            exp_h += measure_text(f"\u2022  {hl}", FONT, 8.5, 11, indent=8)
        exp_h += 4  # gap between jobs
    sections.append(("Experience", exp_h))

    edu_h = len(data["education"]) * 12
    sections.append(("Education", edu_h))

    cert_h = len(data.get("certifications", [])) * 12
    if cert_h:
        sections.append(("Certifications", cert_h))

    lang_h = 12
    sections.append(("Languages", lang_h))

    section_header_h = 16  # space for divider + title per section
    total_content = header_h + sum(sh + section_header_h for _, sh in sections)
    remaining = usable - total_content
    n_gaps = len(sections)  # gaps between header and each section
    extra_gap = max(remaining / n_gaps, 0) if n_gaps else 0
    # Cap extra gap so it doesn't look too loose
    extra_gap = min(extra_gap, 18)

    # --- Pass 2: render --- #
    y = top

    # Background
    c.setFillColor(COLOR_BG)
    c.rect(0, 0, w, h, fill=1, stroke=0)

    def text(s, font=FONT, size=9, spacing=12, color=COLOR_TEXT, indent=0):
        nonlocal y
        c.setFillColor(color)
        c.setFont(font, size)
        avail = max_text - indent
        words = s.split()
        line = ""
        for word in words:
            test = f"{line} {word}".strip()
            if c.stringWidth(test, font, size) > avail:
                if y < bottom:
                    c.showPage()
                    c.setFillColor(COLOR_BG)
                    c.rect(0, 0, w, h, fill=1, stroke=0)
                    y = top
                    c.setFillColor(color)
                    c.setFont(font, size)
                c.drawString(left + indent, y, line)
                y -= spacing
                line = word
            else:
                line = test
        if line:
            if y < bottom:
                c.showPage()
                c.setFillColor(COLOR_BG)
                c.rect(0, 0, w, h, fill=1, stroke=0)
                y = top
                c.setFillColor(color)
                c.setFont(font, size)
            c.drawString(left + indent, y, line)
            y -= spacing

    def section(title):
        nonlocal y
        y -= extra_gap
        c.setStrokeColor(HexColor("#e5e5e5"))
        c.setLineWidth(0.6)
        c.line(left, y + 10, right, y + 10)
        y -= 2
        text(title, FONT_BOLD, 10.5, 14, COLOR_H2)

    # Name
    text(data["personal"]["name"], FONT_BOLD, 17, 19, COLOR_TITLE)
    text(
        f"{data['personal']['title']}  |  {data['personal']['location']}",
        FONT, 9, 13, COLOR_H3,
    )
    text(
        f"{data['personal']['email']}  |  {data['personal']['phone']}",
        FONT, 9, 14, COLOR_TEXT,
    )

    # Summary
    section("Summary")
    text(data["summary"])

    # Skills
    section("Skills")
    for cat, skills in data["skills"].items():
        label = "".join(f" {ch}" if ch.isupper() else ch for ch in cat).strip().title()
        text(f"{label}: {', '.join(skills)}", FONT, 8.5, 11)

    # Experience
    section("Experience")
    for job in data["experience"]:
        end = job["endDate"] if job["endDate"] != "present" else "Present"
        text(
            f"{job['role']} \u2014 {job['company']}  ({job['startDate']} \u2013 {end})",
            FONT_BOLD, 9, 12, COLOR_TEXT,
        )
        for hl in job["highlights"][:3]:
            text(f"\u2022  {hl}", FONT, 8.5, 11, COLOR_TEXT, indent=8)
        y -= 4

    # Education
    section("Education")
    for edu in data["education"]:
        text(f"{edu['degree']} in {edu['field']},  {edu['institution']}  ({edu['year']})", FONT_BOLD, 9, 12, COLOR_TEXT)

    # Certifications
    if data.get("certifications"):
        section("Certifications")
        for cert in data["certifications"]:
            text(f"{cert['name']} \u2014 {cert['issuer']}")

    # Languages
    if data.get("languages"):
        section("Languages")
        text("  |  ".join(f"{l['name']} ({l['level']})" for l in data["languages"]))

    c.save()
    print(f"Generated {PDF_PATH}")


def generate():
    data = json.loads(RESUME_JSON.read_text())

    lines = []

    # Personal info
    p = data["personal"]
    lines.append(f"# {p['name']}")
    lines.append(f"**{p['title']}** | {p['location']}  ")
    lines.append(f"{p['email']} | {p['phone']}\n")

    # Summary
    lines.append("## Summary\n")
    lines.append(data["summary"] + "\n")

    # Skills
    lines.append("## Skills\n")
    for category, skills in data["skills"].items():
        label = category[0].upper() + category[1:]
        # Convert camelCase to spaced words
        label = "".join(f" {c}" if c.isupper() else c for c in label).strip()
        lines.append(f"**{label}**: {', '.join(skills)}  ")
    lines.append("")

    # Experience
    lines.append("## Experience\n")
    for job in data["experience"]:
        end = job["endDate"] if job["endDate"] != "present" else "Present"
        lines.append(f"### {job['role']} — {job['company']}")
        lines.append(f"*{job['location']} | {job['startDate']} – {end}*\n")
        lines.append(f"{job['description']}\n")
        for h in job["highlights"]:
            lines.append(f"- {h}")
        lines.append("")

    # Projects
    if data.get("projects"):
        lines.append("## Projects\n")
        for proj in data["projects"]:
            url_part = ""
            if proj.get("url"):
                link_text = proj.get("name") if proj.get("name") else "project"
                # show short link text like `python_api` instead of full URL
                if "github.com" in proj["url"]:
                    repo_name = proj["url"].rstrip("/").split("/")[-1]
                    link_text = repo_name
                url_part = f" — [{link_text}]({proj['url']})"
            lines.append(f"### {proj['name']}{url_part}")
            lines.append(f"*{', '.join(proj['technologies'])}*\n")
            lines.append(f"{proj['description']}\n")
            for h in proj["highlights"]:
                lines.append(f"- {h}")
            lines.append("")

    # Education
    lines.append("## Education\n")
    for edu in data["education"]:
        lines.append(f"**{edu['degree']} in {edu['field']}**  ")
        lines.append(f"{edu['institution']}, {edu['location']} ({edu['year']})\n")

    # Certifications
    if data.get("certifications"):
        lines.append("## Certifications\n")
        for cert in data["certifications"]:
            lines.append(f"- **{cert['name']}** — {cert['issuer']}")
        lines.append("")

    # Languages
    if data.get("languages"):
        lines.append("## Languages\n")
        langs = [f"{l['name']} ({l['level']})" for l in data["languages"]]
        lines.append(" | ".join(langs) + "\n")

    # Download as PDF
    lines.append("## Download as PDF\n")
    lines.append('<a class="pdf-download-btn" href="../pdf/resume.pdf" download>Download as PDF</a>\n')

    RESUME_MD.write_text("\n".join(lines))
    print(f"Generated {RESUME_MD}")

    # Also generate the PDF
    generate_pdf(data)


if __name__ == "__main__":
    generate()
