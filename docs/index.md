# Titash Roy Choudhury - Resume

Welcome to my **automated resume publishing system**! This documentation covers the complete setup, testing, and deployment process.

## 🚀 Quick Start

Your resume is **automatically published** whenever you make changes:

```
Edit resume.json → Push to GitHub → GitHub Actions builds & deploys → Live at https://titash.github.io/
```

## ✨ Features

- **📄 JSON Resume Storage** - Keep your resume as clean JSON data
- **🤖 Auto-Generation** - PDF generated automatically using Puppeteer
- **📱 Responsive Design** - Works on all devices
- **🔄 CI/CD Pipeline** - Automatic deployment on every push
- **📚 Documentation** - Complete setup and testing guides
- **🎨 Beautiful Design** - Professional gradient homepage with dark mode

## 📦 What's Included

| Component | Purpose |
|-----------|---------|
| `resume.json` | Structured resume data with experience, skills, projects |
| `scripts/generate-pdf.js` | Puppeteer script to convert JSON → PDF |
| `public/index.html` | Beautiful homepage with download button |
| `.github/workflows/deploy.yml` | GitHub Actions CI/CD automation |
| `docs/` | Complete documentation with mkdocs |

## 🎯 Next Steps

1. **[Setup Guide](getting-started/setup.md)** - Initial configuration and deployment
2. **[Local Testing](getting-started/local-testing.md)** - Test locally before publishing
3. **[System Overview](system/overview.md)** - Understand the architecture
4. **[API Reference](api/resume-json.md)** - resume.json structure

## 📊 Current Status

- **Name**: Titash Roy Choudhury
- **Title**: Senior Cloud Data Engineer @ SEB
- **Experience**: 6+ years across multiple companies
- **Skills**: Cloud, Data Engineering, DevOps, and more
- **Location**: Stockholm, Sweden

## 💡 How It Works

```
┌─────────────────────────────────────────────────┐
│          You edit resume.json                    │
│             (locally or on GitHub)               │
└────────────────┬────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────┐
│     GitHub Actions Workflow Triggered           │
│  (on every push to main branch)                  │
└────────────────┬────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────┐
│  Step 1: Setup Node.js & Install Dependencies   │
│  Step 2: Run Puppeteer PDF Generation Script    │
│  Step 3: Generate Documentation (mkdocs)        │
│  Step 4: Deploy to GitHub Pages                 │
└────────────────┬────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────┐
│    Live at https://titash.github.io/            │
│  - Homepage with download button                │
│  - Generated PDF resume                         │
│  - Documentation site                           │
└─────────────────────────────────────────────────┘
```

## 📖 Documentation

- **[Setup Guide](getting-started/setup.md)** - Complete step-by-step setup
- **[Local Testing](getting-started/local-testing.md)** - Test before publishing
- **[Quick Reference](getting-started/quick-reference.md)** - Common commands
- **[System Overview](system/overview.md)** - How everything works together
- **[Architecture](system/architecture.md)** - Technical architecture
- **[File Structure](system/file-structure.md)** - Repository layout
- **[Resume JSON API](api/resume-json.md)** - JSON schema and structure

## 🔧 Technologies

- **Node.js 18** - JavaScript runtime
- **Puppeteer 24.36.1** - Browser automation for PDF generation
- **GitHub Actions** - CI/CD automation
- **GitHub Pages** - Static hosting
- **mkdocs** - Documentation site generator
- **Material Theme** - Beautiful mkdocs theme

## 📝 Editing Your Resume

### Quick Edit (Online)
1. Go to https://github.com/titash/titash.github.io
2. Click `resume.json`
3. Click ✏️ (Edit)
4. Make changes
5. Commit

### Local Edit
1. Clone the repository
2. Edit `resume.json` locally
3. Test with `npm run generate-pdf`
4. Commit and push

**Both automatically trigger deployment within 2-3 minutes!**

## 🎓 Learning Resources

- [mkdocs Documentation](https://www.mkdocs.org/)
- [Material for mkdocs](https://squidfunk.github.io/mkdocs-material/)
- [Puppeteer Documentation](https://pptr.dev/)
- [GitHub Actions Guide](https://docs.github.com/en/actions)
- [GitHub Pages Guide](https://pages.github.com/)

## 💬 Support

Need help? Check these resources:
1. **[Local Testing Guide](getting-started/local-testing.md)** - Debug local issues
2. **[System Overview](system/overview.md)** - Understand the system
3. **[GitHub Actions Logs](https://github.com/titash/titash.github.io/actions)** - Check deployment logs

---

**Last Updated**: Automatically generated on every push

**Live Site**: https://titash.github.io/
