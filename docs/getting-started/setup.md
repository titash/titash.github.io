# Setup Guide

Complete step-by-step guide to set up your resume auto-publishing system.

## Overview

Your resume is stored as **JSON**, automatically generated as **PDF and HTML**, and deployed to GitHub Pages whenever you push changes.

```
Edit resume.json → Push to GitHub → GitHub Actions builds & deploys → Live!
```

---

## Step 1: Prepare Your GitHub Repository

### Option A: Use Existing Repository (Recommended)

If you already have a `titash.github.io` repository:

```bash
cd ~/path/to/titash.github.io
git pull origin main
```

### Option B: Create New Repository

1. Go to https://github.com/new
2. Name it: `[username].github.io` (e.g., `titash.github.io`)
3. Make it **Public**
4. Clone locally:

```bash
git clone https://github.com/[username]/[username].github.io
cd [username].github.io
```

---

## Step 2: Copy Resume Files

Copy the necessary files from the resume template:

```bash
# From your repository root

# 1. Copy resume data
cp /path/to/resume/resume.json .

# 2. Create directories
mkdir -p .github/workflows
mkdir -p scripts
mkdir -p public/pdfs
mkdir -p docs

# 3. Copy GitHub Actions workflow
cp /path/to/resume/.github/workflows/deploy.yml .github/workflows/

# 4. Copy PDF generation script
cp /path/to/resume/scripts/generate-pdf.js scripts/

# 5. Copy homepage
cp /path/to/resume/public/index.html public/
```

---

## Step 3: Set Up Node.js & Dependencies

```bash
# Initialize npm if not already done
npm init -y

# Add dependencies to package.json
npm install puppeteer
```

Your `package.json` should include:

```json
{
  "scripts": {
    "generate-pdf": "node scripts/generate-pdf.js"
  },
  "dependencies": {
    "puppeteer": "^24.36.1"
  }
}
```

---

## Step 4: Set Up mkdocs

!!! note
    mkdocs requires Python. If you don't have Python installed, see [Python Installation](../system/overview.md#requirements).

```bash
# Install mkdocs and theme
pip install mkdocs mkdocs-material

# Copy mkdocs configuration
cp mkdocs.yml .

# Build documentation (optional - GitHub Actions will do this automatically)
mkdocs build
```

Your `mkdocs.yml` should be configured correctly (already included).

---

## Step 5: Create GitHub Pages Configuration

Create `.nojekyll` file in repository root:

```bash
touch .nojekyll
git add .nojekyll
```

---

## Step 6: Configure GitHub Pages

1. Go to your repository on GitHub
2. Navigate to **Settings** → **Pages**
3. **Source**: `Deploy from a branch`
4. **Branch**: Select your main branch (usually `main`)
5. **Folder**: `/root` or `/docs`
6. **Enforce HTTPS**: ✅ Checked
7. Click **Save**

!!! tip
    GitHub Pages may take 1-2 minutes to initialize on first setup. Subsequent updates are usually faster.

---

## Step 7: Verify File Structure

Check that your repository looks like this:

```
.
├── .github/
│   └── workflows/
│       └── deploy.yml
├── scripts/
│   └── generate-pdf.js
├── public/
│   ├── index.html
│   └── pdfs/
├── docs/
│   ├── index.md
│   ├── getting-started/
│   ├── system/
│   └── api/
├── resume.json
├── mkdocs.yml
├── .nojekyll
├── package.json
└── .gitignore
```

---

## Step 8: Deploy to GitHub

```bash
# Stage all files
git add .

# Commit with descriptive message
git commit -m "feat: Add resume auto-publishing with mkdocs documentation"

# Push to GitHub
git push origin main
```

---

## Step 9: Monitor Deployment

1. Go to your repository on GitHub
2. Click on **Actions** tab
3. Watch the workflow run
4. Once complete (✅), your sites will be available at:
   - **Homepage**: `https://[username].github.io/`
   - **Documentation**: `https://[username].github.io/docs/`
   - **Resume PDF**: `https://[username].github.io/resume.pdf`

!!! info
    First deployment may take 2-5 minutes. Subsequent updates are faster (1-2 minutes).

---

## Step 10: Test Everything

### Test 1: Download Resume PDF
- Visit `https://[username].github.io/`
- Click **📥 Download PDF**
- Verify PDF opens and looks good

### Test 2: View Homepage
- Visit `https://[username].github.io/`
- Check that it displays your name and contact info
- Hover over buttons to see animations

### Test 3: Access Documentation
- Visit `https://[username].github.io/docs/`
- Navigate through different sections
- Search for content using the search box

### Test 4: Make a Test Update
- Edit `resume.json` locally or on GitHub
- Change something small (e.g., add a project name)
- Push the change
- Watch GitHub Actions automatically build and deploy
- Verify the change appears on the website

---

## Customization

### Change Your Name & Contact Info

Edit `resume.json`:

```json
{
  "personal": {
    "name": "Your Name",
    "title": "Your Title",
    "email": "your.email@example.com",
    "phone": "+1-234-567-8900",
    "location": "Your City, Country",
    "company": "Your Company",
    "visaStatus": "Visa Status"
  }
}
```

### Add Your Experience

Edit the `experience` array in `resume.json`:

```json
{
  "experience": [
    {
      "role": "Your Job Title",
      "company": "Company Name",
      "location": "City",
      "startDate": "2020-01-15",
      "endDate": "present",
      "description": "Brief description",
      "highlights": [
        "Achievement 1",
        "Achievement 2"
      ]
    }
  ]
}
```

### Customize the Homepage

Edit `public/index.html` to change colors, text, and layout.

### Customize Documentation

Edit or create files in the `docs/` folder. Changes are automatically reflected in the documentation site.

---

## Troubleshooting

### GitHub Pages not showing up

- Ensure `.nojekyll` file exists
- Check GitHub Pages is enabled in Settings
- Wait 1-2 minutes for initial setup
- Clear your browser cache

### PDF not generating

- Check `resume.json` is valid JSON
- Run `npm run generate-pdf` locally to test
- Check GitHub Actions logs for errors

### Documentation not building

- Ensure `mkdocs.yml` is in repository root
- Check all markdown files have proper frontmatter
- Verify Python and mkdocs are installed

---

## Next Steps

1. ✅ Setup complete!
2. 📝 Edit `resume.json` with your information
3. 🧪 Follow the [Local Testing Guide](./local-testing.md) to verify everything works
4. 🚀 Push to GitHub and watch it deploy automatically

See [Quick Reference](./quick-reference.md) for common commands.
