# titash.github.io

Personal blog and resume built with [MkDocs Simple Blog](https://github.com/FernandoCelmer/mkdocs-simple-blog).

## Prerequisites

- [uv](https://docs.astral.sh/uv/) (Python package manager)

## Quick Start

```bash
# Install dependencies
uv sync

# Start local dev server (http://localhost:8000), auto-killing any previous server
bash scripts/serve.sh

# (Alternative explicit command)
# pkill -f "mkdocs serve" 2>/dev/null && uv run mkdocs serve
```

## Adding a New Blog Post

1. Create a markdown file in `docs/blog/`:

   ```
   docs/blog/my-new-post.md
   ```

2. Write your content with a title:

   ```markdown
   # My New Post

   Your content here...
   ```

3. Add it to the nav in `mkdocs.yml`:

   ```yaml
   nav:
     - Home: index.md
     - Resume: resume.md
     - Blog:
       - blog/my-new-post.md
       - blog/hello-world.md
   ```

## Updating the Resume

1. Edit `resume.json` with your updated information.
2. Regenerate the markdown and PDF:

   ```bash
   uv run python scripts/generate_resume.py
   ```

   This produces both `docs/resume.md` and `docs/pdf/resume.pdf` in one step.

3. Preview locally with `bash scripts/serve.sh`.

## Deploying to GitHub Pages

```bash
uv run mkdocs gh-deploy
```

This builds the site and pushes it to the `gh-pages` branch. Set your repo's GitHub Pages source to the `gh-pages` branch in **Settings → Pages**.

## Project Structure

```
├── docs/                    # Source content
│   ├── index.md             # Home page
│   ├── resume.md            # Generated from resume.json
│   ├── blog/
│   │   └── hello-world.md    # Blog posts go here
│   └── stylesheets/
│       └── resume.css       # Resume & print styles
├── scripts/
│   └── generate_resume.py   # Converts resume.json → resume.md
├── resume.json              # Resume data (single source of truth)
└── mkdocs.yml               # Site configuration
```
