# Titash Roy Choudhury - Resume

Professional resume website built with **MkDocs** + **GitHub Pages**. Single source of truth: `resume.json`.

## Features

✨ **Minimal & Fast** — Just your resume, no bloat  
📝 **Auto-Generated** — Generated from `resume.json`  
📄 **Print to PDF** — Use browser's print function (Ctrl+P)  
🚀 **Auto-Deploy** — GitHub Actions deploys on every git push  
📱 **Responsive** — Works perfectly on all devices  

## Quick Start

### Local Development

```bash
# Generate resume from resume.json
npm run build-resume

# Start dev server
mkdocs serve
```

Visit **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** in your browser.

### Update Your Resume

```bash
# 1. Edit resume.json
# 2. Generate markdown
npm run build-resume

# 3. View changes immediately (if server running)
```

### Download as PDF

From the website (local or GitHub Pages):
1. Press **Ctrl+P** (Windows/Linux) or **Cmd+P** (Mac)
2. Click "Save as PDF"
3. Done!

## Folder Structure

```
.
├── docs/
│   └── index.md              # Auto-generated from resume.json
├── scripts/
│   └── json-to-md.js         # JSON → Markdown converter
├── .github/workflows/
│   └── deploy.yml            # Auto-deployment on push
├── resume.json               # Your resume data
├── mkdocs.yml                # Site config
└── package.json              # Build scripts
```

## Deployment

Push to `main` branch → GitHub Actions automatically:
1. Generates resume.md from resume.json
2. Builds MkDocs site
3. Deploys to GitHub Pages

No manual steps needed!

## GitHub Pages Setup

Make sure GitHub Pages is enabled:
1. **Settings** → **Pages**
2. Set source to **Deploy from a branch**
3. Select **gh-pages** branch

The workflow creates and updates the `gh-pages` branch automatically.

## Workflow

1. **Edit** `resume.json` with your latest info
2. **Run** `npm run build-resume` (generates `docs/index.md`)
3. **Push** to GitHub
4. **Done!** Site auto-builds and deploys

## Performance

- **Build time**: ~90ms
- **Site size**: ~1.4MB (with readthedocs theme)
- **Zero bloat**: Only MkDocs + search
- **Fast CDN**: GitHub Pages hosting

## License

See [LICENSE](LICENSE) file.
