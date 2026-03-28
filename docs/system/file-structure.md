# File Structure

Understanding the repository layout and file organization.

## Complete Directory Tree

```
titash.github.io/
│
├── .github/                              # GitHub configuration
│   └── workflows/
│       └── deploy.yml                   # GitHub Actions CI/CD workflow
│
├── scripts/                              # Build scripts
│   └── generate-pdf.js                  # Puppeteer PDF generation
│
├── public/                               # Public static files
│   ├── index.html                        # Homepage (landing page)
│   ├── resume.pdf                        # Generated PDF (auto-created)
│   └── pdfs/
│       └── Titash_Resume.pdf             # Storage for PDFs
│
├── docs/                                 # Documentation source (mkdocs)
│   ├── index.md                          # Home page
│   ├── getting-started/
│   │   ├── setup.md                      # Setup instructions
│   │   ├── local-testing.md              # Testing guide
│   │   └── quick-reference.md            # Quick commands
│   ├── system/
│   │   ├── overview.md                   # System overview
│   │   ├── architecture.md               # Technical architecture
│   │   └── file-structure.md             # This file
│   └── api/
│       └── resume-json.md                # Resume JSON schema
│
├── site/                                 # Built documentation (auto)
│   ├── index.html                        # Generated HTML
│   ├── getting-started/
│   ├── system/
│   ├── api/
│   ├── search/
│   └── assets/
│       ├── css/
│       ├── js/
│       └── fonts/
│
├── resume.json                           # 📝 YOUR DATA (EDIT THIS!)
├── mkdocs.yml                            # Documentation configuration
├── package.json                          # Node.js dependencies
├── package-lock.json                     # Locked dependency versions
├── .nojekyll                             # GitHub Pages config
│
└── (other files)
    ├── .gitignore                        # Git ignore rules
    ├── .gitattributes                    # Git attributes
    ├── LICENSE                           # License file
    ├── README.md                         # Repository readme
    └── LOCAL_TESTING.md                  # Testing documentation
```

---

## File Details

### Configuration Files

#### `mkdocs.yml`

```yaml
# Main documentation configuration
site_name: Your Site Title
nav:
  - Home: index.md
  - Getting Started:
    - Setup: getting-started/setup.md
plugins:
  - search
theme:
  name: material
```

**Purpose**: Configures mkdocs documentation site

**When to edit**: 
- Change site title/description
- Add new documentation sections
- Change theme colors or features

---

#### `package.json`

```json
{
  "name": "resume-site",
  "version": "1.0.0",
  "scripts": {
    "generate-pdf": "node scripts/generate-pdf.js"
  },
  "dependencies": {
    "puppeteer": "^24.36.1"
  }
}
```

**Purpose**: Defines Node.js dependencies and scripts

**When to edit**: 
- Add new npm packages
- Update script commands
- Change versions

---

#### `.nojekyll`

```
(empty file)
```

**Purpose**: Tells GitHub Pages not to use Jekyll

**When to edit**: Never (keep empty)

---

### Data Files

#### `resume.json` - **⭐ MOST IMPORTANT**

```json
{
  "personal": {
    "name": "Your Name",
    "title": "Your Title",
    "email": "your@email.com",
    "phone": "+1-234-567-8900",
    "location": "City, Country",
    "company": "Current Company",
    "visaStatus": "Your Visa Status"
  },
  "summary": "Your professional summary...",
  "skills": {
    "cloud": ["AWS", "GCP", "Azure"],
    "languages": ["Python", "JavaScript", "SQL"]
  },
  "experience": [
    {
      "role": "Senior Engineer",
      "company": "Company Name",
      "location": "City",
      "startDate": "2020-01-01",
      "endDate": "present",
      "description": "Brief role description",
      "highlights": ["Achievement 1", "Achievement 2"]
    }
  ],
  "projects": [...],
  "education": [...],
  "certifications": [...]
}
```

**Purpose**: Single source of truth for your resume data

**When to edit**: 
- Whenever you update your resume
- Add new experience
- Update skills
- Add projects or certifications

**⚠️ Important**: 
- Keep valid JSON format
- Use ISO 8601 dates (YYYY-MM-DD)
- Keep updated to latest info

See [API Reference](../api/resume-json.md) for full schema.

---

### Build Scripts

#### `scripts/generate-pdf.js`

```javascript
const puppeteer = require('puppeteer');
const http = require('http');
const fs = require('fs');

// Starts local server, renders resume, generates PDF
async function generatePDF() {
  // ... implementation
}
```

**Purpose**: Generates PDF from resume.json using Puppeteer

**When to edit**: 
- Change PDF styling
- Modify template layout
- Add sections or fields
- Change output path

**Don't edit if**: Working normally

---

### Website Files

#### `public/index.html`

```html
<!DOCTYPE html>
<html>
<head>
  <title>Your Name - Resume</title>
  <style> /* ... styling ... */ </style>
</head>
<body>
  <div class="container">
    <h1>Your Name</h1>
    <a href="/resume.pdf">Download PDF</a>
  </div>
</body>
</html>
```

**Purpose**: Homepage that visitors see first

**When to edit**: 
- Change colors or styling
- Update personal info
- Modify button text
- Add social links

---

#### `public/resume.pdf`

```
(Binary PDF file)
```

**Purpose**: Generated PDF resume (auto-created by GitHub Actions)

**When to edit**: Never (auto-generated)

---

### Documentation Files

#### `docs/index.md`

```markdown
# Titash Roy Choudhury - Resume

Welcome to my resume site...

## Quick Start
## Features
## Technologies
```

**Purpose**: Main documentation page

**When to edit**: Update introduction, add resources

---

#### `docs/getting-started/setup.md`

Complete setup guide with step-by-step instructions.

**When to edit**: Update setup process, add troubleshooting

---

#### `docs/getting-started/local-testing.md`

Local testing guide with 8-step verification process.

**When to edit**: Add new tests, update troubleshooting

---

#### `docs/system/overview.md`

System architecture and technology overview.

**When to edit**: Document system changes, update tech stack

---

### Workflow Files

#### `.github/workflows/deploy.yml`

```yaml
name: Deploy Resume to GitHub Pages

on:
  push:
    branches: [ main ]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '18'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Generate PDF
        run: npm run generate-pdf
      
      # ... more steps
```

**Purpose**: GitHub Actions pipeline for CI/CD

**When to edit**: 
- Update Node.js version
- Add build steps
- Change deployment options
- Fix failing actions

**Critical**: Keep correct action versions (v3/v4, not v2/v3)

---

### Build Output

#### `site/` (Generated)

```
site/
├── index.html              # Generated from docs/index.md
├── getting-started/
│   ├── setup/index.html
│   ├── local-testing/index.html
│   └── quick-reference/index.html
├── system/
├── api/
├── assets/
│   ├── css/                # Material theme CSS
│   ├── js/                 # Material theme JS
│   └── fonts/              # Material fonts
└── search/                 # Search index
```

**Purpose**: Built documentation (auto-generated by mkdocs)

**When to check**: After `mkdocs build`

**Don't edit**: Auto-generated from markdown

---

## File Size Reference

Typical file sizes:

```
resume.json                    10-50 KB
scripts/generate-pdf.js        15-20 KB
public/index.html              4-8 KB
mkdocs.yml                      1-3 KB
package.json                    500 B
.github/workflows/deploy.yml    2-4 KB
docs/index.md                   5-10 KB
docs/getting-started/           50-100 KB (all combined)
docs/system/                    80-150 KB (all combined)
site/ (built)                   300-500 KB (all combined)
resume.pdf (generated)          100-500 KB
```

---

## What Gets Deployed

### To GitHub Pages

When you push or GitHub Actions runs:

```
Deployed to https://titash.github.io/
├── public/index.html       → /index.html
├── public/resume.pdf       → /resume.pdf
├── site/*                  → /docs/*
└── Resume PDF              → /resume.pdf
```

### Deployed Content

```
https://titash.github.io/
  ├── / (index.html)
  │   └── Homepage with download button
  │
  ├── /resume.pdf
  │   └── Generated PDF resume
  │
  └── /docs/
      └── Documentation site (mkdocs)
          ├── /docs/ → search
          ├── /docs/getting-started/*
          └── /docs/system/*
```

---

## What Doesn't Get Deployed

Files that are NOT deployed:

```
❌ node_modules/          (ignored, too large)
❌ .git/                  (ignored, not web content)
❌ .github/               (ignored, meta-data only)
❌ scripts/               (ignored, build tools only)
❌ Local generated PDF    (temporary, not committed)
❌ .gitignore             (ignored, config file)
❌ *.local                (ignored files)
```

---

## Important Patterns

### Do's ✅

- ✅ Keep resume.json updated
- ✅ Commit changes to Git
- ✅ Use markdown for documentation
- ✅ Keep JSON valid
- ✅ Use relative paths in links
- ✅ Test locally before pushing

### Don'ts ❌

- ❌ Don't commit personal passwords
- ❌ Don't manually edit deploy.yml unless fixing
- ❌ Don't manually upload to GitHub Pages
- ❌ Don't edit the `site/` folder (auto-generated)
- ❌ Don't commit node_modules/
- ❌ Don't put sensitive data in resume.json

---

## Editing Workflow

```
1. Edit resume.json locally
          ↓
2. Validate JSON (jsonlint.com)
          ↓
3. Test locally: npm run generate-pdf
          ↓
4. Review generated PDF
          ↓
5. Stage: git add resume.json
          ↓
6. Commit: git commit -m "Update: ..."
          ↓
7. Push: git push origin main
          ↓
8. GitHub Actions auto-builds & deploys
          ↓
9. Live within 2-3 minutes
```

---

## File Organization Principles

### Separation of Concerns

```
resume.json         Data layer
generate-pdf.js     Generation layer
public/index.html   Presentation layer
docs/               Documentation layer
.github/workflows/  Automation layer
```

### Single Responsibility

```
mkdocs.yml          Configuration only
package.json        Dependencies only
.nojekyll           Jekyll config only
deploy.yml          CI/CD pipeline only
```

### Easy Navigation

```
docs/               All documentation
scripts/            All build scripts
public/             All web files
.github/            All GitHub config
```

---

## Adding New Files

If you need to add new content:

### Adding Documentation

1. Create `docs/section/page.md`
2. Update `mkdocs.yml` nav section
3. Link from other pages
4. Push to GitHub
5. Auto-builds documentation

### Adding Dependencies

1. Edit `package.json`
2. Run `npm install`
3. Update scripts if needed
4. Commit and push

### Adding Sections to Resume

1. Edit `resume.json`
2. Add to appropriate section
3. Test: `npm run generate-pdf`
4. Commit and push

---

## Version Control

### What's Committed

```
✅ resume.json
✅ scripts/
✅ public/
✅ docs/
✅ mkdocs.yml
✅ package.json
✅ package-lock.json
✅ .github/workflows/
✅ .gitignore
```

### What's Not Committed

```
❌ node_modules/          (in .gitignore)
❌ site/                  (auto-generated)
❌ *.local               (in .gitignore)
❌ resume.pdf            (local temp)
❌ .env                  (in .gitignore)
```

---

## Performance Considerations

### File Size Best Practices

```
keep resume.json < 50 KB
keep individual docs < 100 KB
keep images < 500 KB (if any)
keep PDF < 500 KB
```

### Build Time Optimization

```
Faster builds:
├── Smaller resume.json
├── Fewer docs pages
├── Remove large images
└── Use GitHub Actions caching
```

---

## Recovery & Cleanup

### If Something Goes Wrong

```
1. Check what changed: git status
2. Undo changes: git checkout resume.json
3. Check history: git log --oneline
4. Revert if needed: git revert [hash]
5. Push fix: git push origin main
```

### Clean Up Repo

```bash
# Remove untracked files (safe)
git clean -fd

# Remove ignored files
git clean -fdX

# Check what would be removed
git clean -fdn
```

---

## References

- [How to edit files on GitHub](https://docs.github.com/en/repositories/working-with-files)
- [Git basics](https://git-scm.com/book/en/v2)
- [mkdocs file layout](https://www.mkdocs.org/user-guide/file-layout/)
- [GitHub Actions workflows](https://docs.github.com/en/actions/using-workflows)

---

**File Structure Version**: 1.0

**Last Updated**: March 28, 2026

**Total Files**: 20+

**Total Size**: ~1-2 MB (including dependencies)
