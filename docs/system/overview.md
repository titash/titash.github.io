# System Overview

Complete technical overview of the resume auto-publishing system.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    User Workflow                            │
│  Edit resume.json locally or on GitHub                      │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                  GitHub Repository                          │
│  ├── resume.json (source data)                             │
│  ├── scripts/generate-pdf.js (PDF generator)               │
│  ├── public/index.html (website)                           │
│  ├── docs/ (documentation source)                          │
│  ├── .github/workflows/deploy.yml (automation)             │
│  └── mkdocs.yml (docs config)                              │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼ (Git push triggers webhook)
┌─────────────────────────────────────────────────────────────┐
│              GitHub Actions Pipeline                        │
│  1. Checkout code                                           │
│  2. Setup Node.js 18                                        │
│  3. Install dependencies (npm install)                      │
│  4. Generate PDF (Puppeteer from resume.json)              │
│  5. Build documentation (mkdocs build)                      │
│  6. Prepare deployment files                                │
│  7. Deploy to GitHub Pages                                  │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│               GitHub Pages (Static Hosting)                 │
│  ├── https://titash.github.io/                             │
│  │   ├── index.html (homepage with download button)        │
│  │   ├── resume.pdf (generated PDF)                        │
│  │   └── /docs/ (documentation site)                       │
└─────────────────────────────────────────────────────────────┘
```

---

## How It Works

### 1. Data Storage

Your resume is stored as **JSON**:
- Clean, structured format
- Easy to edit and validate
- Version controlled via Git
- Human-readable

### 2. PDF Generation

**Puppeteer** generates PDF from resume.json:
- Runs in headless Chrome/Firefox
- Renders from HTML template
- Creates professional PDF
- Happens automatically on each push

### 3. Website

**GitHub Pages** serves your resume:
- Static hosting (free)
- Custom domain support
- HTTPS enabled
- Auto-deploys from GitHub

### 4. Documentation

**mkdocs** creates documentation site:
- Converts markdown to beautiful HTML
- Responsive design
- Search functionality
- Dark mode support

---

## Technology Stack

### Runtime & Build

| Technology | Version | Purpose |
|-----------|---------|---------|
| **Node.js** | 18 | JavaScript runtime |
| **npm** | 9+ | Package manager |
| **Puppeteer** | 24.36.1 | Headless browser for PDF |
| **mkdocs** | 1.5+ | Documentation generator |
| **Material Theme** | Latest | Beautiful mkdocs theme |

### Infrastructure

| Service | Purpose |
|---------|---------|
| **GitHub** | Version control & repository hosting |
| **GitHub Actions** | CI/CD automation |
| **GitHub Pages** | Static website hosting |
| **Git** | Version control system |

### Files & Format

| Format | Usage |
|--------|-------|
| **JSON** | Resume data storage |
| **JavaScript** | Build scripts (Puppeteer) |
| **HTML** | Website and PDF template |
| **CSS** | Styling |
| **Markdown** | Documentation |
| **YAML** | Configuration (GitHub Actions, mkdocs) |

---

## Data Flow

```
1. resume.json (JSON source data)
         ▼
2. generate-pdf.js reads JSON
         ▼
3. Generates HTML from template
         ▼
4. Puppeteer renders to PDF
         ▼
5. Saves Titash_Resume.pdf
         ▼
6. Deploy to https://titash.github.io/resume.pdf
```

---

## Deployment Process

### Triggered By
- Push to main branch
- Manual workflow dispatch
- Scheduled (optional, if configured)

### Steps

1. **Setup** (15-20 seconds)
   - Checkout code
   - Setup Node.js 18
   - Cache dependencies

2. **Build** (30-40 seconds)
   - Install npm packages
   - Generate PDF via Puppeteer
   - Build documentation with mkdocs

3. **Deploy** (20-30 seconds)
   - Prepare deployment files
   - Upload to GitHub Pages
   - Clear cache

**Total Time**: 2-3 minutes

---

## File Organization

```
titash.github.io/
├── .github/
│   └── workflows/
│       └── deploy.yml                 ← CI/CD automation
├── scripts/
│   └── generate-pdf.js                ← PDF generator
├── public/
│   ├── index.html                     ← Homepage
│   ├── resume.pdf                     ← Generated PDF (auto)
│   └── pdfs/
│       └── Titash_Resume.pdf          ← Generated PDF (auto)
├── docs/                              ← Documentation source
│   ├── index.md                       ← Main page
│   ├── getting-started/
│   │   ├── setup.md
│   │   ├── local-testing.md
│   │   └── quick-reference.md
│   ├── system/
│   │   ├── overview.md
│   │   ├── architecture.md
│   │   └── file-structure.md
│   └── api/
│       └── resume-json.md
├── resume.json                        ← Your data (EDIT THIS!)
├── mkdocs.yml                         ← Documentation config
├── package.json                       ← Dependencies
├── .nojekyll                          ← GitHub Pages config
└── .gitignore                         ← Git ignore rules
```

---

## Key Concepts

### Resume as Code

Your resume is **code**:
- Version controlled
- Peer-reviewable
- Automated generation
- Easy to maintain

### Static Site

Your website is **static**:
- Fast loading
- Secure (no database)
- Easy to deploy
- Free hosting with GitHub Pages

### High Availability

System never goes down:
- GitHub pages is redundant
- Always HTTPS
- Global CDN
- Auto-backups

### Continuous Deployment

Changes deploy automatically:
- Push to main → Actions triggered
- PDF generated automatically
- Docs built automatically
- Live within 2-3 minutes

---

## Requirements

### System Requirements

- **Git** - For version control
- **Node.js 18+** - For build tools
- **npm 9+** - For package management
- **Python 3.7+** - For mkdocs (optional, GitHub Actions handles it)
- **Text editor** - VS Code recommended

### Git Setup

```bash
# Configure Git
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Generate SSH key (recommended)
ssh-keygen -t ed25519 -C "your.email@example.com"
# Add public key to GitHub
```

### GitHub Setup

1. Create account at https://github.com
2. Create repository: `[username].github.io`
3. Push code to main branch
4. Enable GitHub Pages in settings

---

## Performance

### Build Time

| Step | Typical Time |
|------|---|
| Setup Environment | 15-20 sec |
| Install Dependencies | 20-30 sec |
| Generate PDF | 10-15 sec |
| Build Documentation | 10-15 sec |
| Deploy | 15-20 sec |
| **Total** | **2-3 minutes** |

### Website Performance

| Metric | Value |
|--------|-------|
| **Page Load** | < 1 second |
| **PDF Download** | < 100KB |
| **Docs Site** | < 500KB |
| **Time to First Byte** | < 200ms |

### Optimization Tips

- Keep resume.json < 50KB
- Compress images if any
- Use CDN (GitHub Pages default)
- Enable browser caching
- Minimize CSS/JS

---

## Security

### What's Secure

- ✅ HTTPS enabled by default
- ✅ No sensitive data exposed
- ✅ GitHub handles authentication
- ✅ Static site (no injection attacks)
- ✅ Automatic backups via Git

### What to Protect

- 🔒 Never commit sensitive data
- 🔒 Don't expose personal addresses
- 🔒 Generate new SSH keys if shared
- 🔒 Keep phone numbers private
- 🔒 Use generic email addresses

### Data Privacy

All data is public (choose what to share):
- Homepage is public
- PDF is public
- Documentation is public
- Resume.json is version controlled

---

## Scalability

System can handle:
- ✅ Unlimited resume updates
- ✅ Multiple resume formats (future)
- ✅ Large PDFs (up to GitHub limits)
- ✅ High traffic (GitHub Pages scale)
- ✅ Multiple repositories

---

## Troubleshooting

### Common Issues

| Issue | Cause | Fix |
|-------|-------|-----|
| PDF not generating | Invalid JSON | Validate at jsonlint.com |
| Docs not building | Missing mkdocs.yml | Ensure file in root |
| Site not deploying | Branch permissions | Check Settings → Pages |
| Actions failing | Dependency error | Check Actions logs |

### Debug Steps

1. Check GitHub Actions logs
2. Validate resume.json
3. Test locally with `npm run generate-pdf`
4. Check mkdocs.yml syntax
5. Verify file permissions

---

## Next Steps

1. Read [Setup Guide](../getting-started/setup.md) for installation
2. Follow [Local Testing](../getting-started/local-testing.md) guide
3. Review [File Structure](./file-structure.md) details
4. Check [API Reference](../api/resume-json.md) for JSON schema
5. See [Architecture](./architecture.md) for technical deep-dive

---

**System:** Automated Resume Publishing with GitHub Pages & mkdocs

**Status:** Production Ready

**Last Updated:** Auto-generated

**Maintenance:** Update resume.json anytime; system handles everything else!
