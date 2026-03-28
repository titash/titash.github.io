# Quick Reference

Common commands and quick setup steps.

## Installation Quick Start

```bash
# Clone repository
git clone https://github.com/[username]/[username].github.io
cd [username].github.io

# Install dependencies
npm install

# Test locally
npm run generate-pdf

# Verify PDF created
ls -lh Titash_Resume.pdf
```

## Common Commands

### Resume Editing

```bash
# Edit locally
nano resume.json

# Validate before committing
node -e "JSON.parse(require('fs').readFileSync('resume.json'))" && echo "Valid"

# Generate PDF to test
npm run generate-pdf

# View generated PDF
open Titash_Resume.pdf

# Clean up before git push
rm Titash_Resume.pdf
```

### Git Workflow

```bash
# Check status
git status

# Stage changes
git add .
git add resume.json                    # Stage specific file

# Commit
git commit -m "Update: Added new role"

# Push
git push origin main

# View recent commits
git log --oneline -5
```

### Documentation

```bash
# Build mkdocs locally
mkdocs build

# Serve locally to preview
mkdocs serve
# Visit: http://localhost:8000

# Stop server
Ctrl + C
```

### Quick Checks

```bash
# Verify all files exist
ls resume.json scripts/generate-pdf.js public/index.html .github/workflows/deploy.yml mkdocs.yml

# Check file sizes
ls -lh resume.json scripts/generate-pdf.js

# Count lines in resume
cat resume.json | wc -l

# View resume structure
cat resume.json | head -30
```

## Edit Methods

### Method 1: Online (Fastest)

1. Go to: https://github.com/[username]/[username].github.io
2. Click: `resume.json`
3. Click: ✏️ (Edit)
4. Make changes
5. Scroll down → Click: "Commit changes"
✅ Auto-deploys in 2-3 minutes

### Method 2: Local (More Control)

```bash
# Make sure you're updated
git pull origin main

# Edit file
nano resume.json

# Test
npm run generate-pdf

# Commit and push
git add resume.json
git commit -m "Update: [description]"
git push origin main
```

### Method 3: VS Code (Recommended)

```bash
# Open in VS Code
code .

# Edit resume.json
# Use Ctrl+Shift+P → Format Document to validate JSON

# Terminal in VS Code
# npm run generate-pdf
# git push origin main
```

## Troubleshooting Quick Fixes

| Issue | Fix |
|-------|-----|
| "module not found" | `npm install` |
| "JSON invalid" | Use https://jsonlint.com |
| "Port 4000 in use" | Kill process: `lsof -ti:4000 \| xargs kill -9` |
| "Permission denied" | `chmod +x scripts/generate-pdf.js` |
| "Git push fails" | `git pull origin main` first |
| "PDF won't generate" | Check resume.json with jsonlint.com |
| "GitHub Actions failing" | Check Actions tab for logs |

## Directory Structure

```
.
├── .github/workflows/deploy.yml     # CI/CD automation
├── scripts/generate-pdf.js          # PDF generator
├── public/
│   ├── index.html                   # Homepage
│   └── pdfs/                        # Generated PDFs
├── docs/                            # Documentation source
│   ├── index.md
│   ├── getting-started/
│   ├── system/
│   └── api/
├── resume.json                       # Your data (EDIT THIS)
├── mkdocs.yml                        # Documentation config
├── package.json                      # Dependencies
└── .nojekyll                         # GitHub Pages config
```

## File Sizes Reference

### Expected Sizes

| File | Expected Size |
|------|---|
| resume.json | 10KB - 50KB |
| Titash_Resume.pdf | 100KB - 500KB |
| generate-pdf.js | 10KB - 20KB |
| mkdocs.yml | 1KB - 5KB |

## URLs

| What | URL |
|------|-----|
| Homepage | https://[username].github.io/ |
| Resume PDF | https://[username].github.io/resume.pdf |
| Documentation | https://[username].github.io/docs/ |
| GitHub Repo | https://github.com/[username]/[username].github.io |
| GitHub Actions | https://github.com/[username]/[username].github.io/actions |

Replace `[username]` with your actual GitHub username.

## Environment Variables

None required for basic setup.

Optional for GitHub Actions:
- `GITHUB_TOKEN` - Usually auto-provided by GitHub Actions

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| puppeteer | ^24.36.1 | PDF generation |
| node | ^18.0.0 | Runtime |
| mkdocs | Latest | Documentation |
| mkdocs-material | Latest | Beautiful theme |

Install with: `npm install`

## Deployment Workflow

```
Edit → Save → Git Add → Commit → Push → GitHub Actions
                                         ↓
                          Build PDF + Docs → Deploy
                                         ↓
                            Live at GitHub Pages
```

Time: ~2-3 minutes from push to live

## Useful Links

- [resume.json spec](../api/resume-json.md)
- [System Overview](../system/overview.md)
- [Architecture](../system/architecture.md)
- [Local Testing](./local-testing.md)
- [Full Setup Guide](./setup.md)

## CI/CD Pipeline

What happens automatically when you push:

1. ✅ GitHub Actions triggered
2. ✅ Node.js 18 set up
3. ✅ Dependencies installed
4. ✅ PDF generated from resume.json
5. ✅ Documentation built from markdown
6. ✅ Static site prepared
7. ✅ Deployed to GitHub Pages
8. ✅ Live within 2-3 minutes

Monitor at: https://github.com/[username]/[username].github.io/actions

## Pro Tips

### Tip 1: Validate Before Pushing
```bash
npm run generate-pdf 2>&1 | grep -i "error\|success"
```

### Tip 2: Keep Backup
```bash
cp resume.json resume.backup.json
```

### Tip 3: Preview Changes
```bash
npm run generate-pdf
open Titash_Resume.pdf
# Review, then: rm Titash_Resume.pdf
```

### Tip 4: Check Git Before Push
```bash
git status                # See what changed
git diff resume.json      # See exact changes
git add resume.json       # Stage specific file
```

### Tip 5: Schedule Updates
Remind yourself to update:
```bash
# Add to your calendar or use:
echo "0 0 1 * * cd ~/path && git -C . pull && npm run generate-pdf" | crontab -
```

## Support

Facing issues? Check:
1. [Local Testing Guide](./local-testing.md) - Debug locally first
2. [System Overview](../system/overview.md) - Understand architecture
3. GitHub Actions Logs - https://github.com/[username]/[username].github.io/actions
4. [API Reference](../api/resume-json.md) - JSON schema

---

**Updated**: Automatically generated

**See Also**: Full guides in [documentation](../index.md)
