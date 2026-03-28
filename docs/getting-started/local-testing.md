# Local Testing Guide

Test your resume locally before publishing to GitHub!

## Prerequisites

Make sure you have:

- **Node.js 18+** - Check with `node --version`
- **npm 9+** - Check with `npm --version`
- **Git** - Check with `git --version`
- **Text editor** - VS Code, Sublime Text, etc.

---

## Testing Checklist

Use this checklist to verify everything works:

```
✅ Dependencies installed
✅ Files in correct locations
✅ PDF generation works
✅ PDF file created
✅ Resume data loaded correctly
✅ JSON is valid
✅ All required fields present
✅ Ready to deploy!
```

---

## Test 1: Install Dependencies

```bash
cd ~/path/to/your-repo

# Install Node.js packages
npm install
```

**Expected output:**
```
added XX packages in Xs
```

**Troubleshoot:**
- If error: Run `npm cache clean --force` then try again
- Check internet connection
- Ensure Node.js is installed: `node --version`

---

## Test 2: Verify File Structure

Check that all required files exist:

```bash
# Test resume.json
ls -lh resume.json
cat resume.json | head -20

# Test PDF script
ls -lh scripts/generate-pdf.js

# Test homepage
ls -lh public/index.html

# Test workflow
ls -lh .github/workflows/deploy.yml

# Test mkdocs config
ls -lh mkdocs.yml
```

**Expected:**
- All files listed with size > 0
- `resume.json` should be 15KB+
- No "No such file or directory" errors

---

## Test 3: Validate JSON

Make sure `resume.json` is valid:

```bash
# Method 1: Node.js validation
node -e "console.log(JSON.parse(require('fs').readFileSync('resume.json')))" && echo "✅ JSON is valid"

# Method 2: Online tool
# Go to https://jsonlint.com and paste your resume.json
```

**Expected output:**
```
✅ JSON is valid
```

**If error:** Check for missing commas or quotes

---

## Test 4: Generate PDF Locally

Generate the PDF and test it:

```bash
# Run the PDF generation script
npm run generate-pdf
```

**Expected output:**
```
Server running on http://localhost:4000
✅ PDF generated successfully: /path/to/Titash_Resume.pdf
```

**Troubleshoot:**
- If port 4000 in use: Kill process or change port in script
- If Puppeteer error: Run `npm install --force puppeteer`
- If file system error: Check write permissions in project directory

---

## Test 5: Verify PDF Output

Check the generated PDF:

```bash
# List the PDF
ls -lh Titash_Resume.pdf

# Check file type
file Titash_Resume.pdf

# Check size is reasonable (100KB - 500KB)
```

**Expected:**
```
-rw-rw-r-- 1 user group 287K Titash_Resume.pdf
Titash_Resume.pdf: PDF document, version 1.4, 3 page(s)
```

**Open the PDF:**
```bash
# macOS
open Titash_Resume.pdf

# Linux (if viewer available)
xdg-open Titash_Resume.pdf

# Or find it in your file manager
```

**Check these in the PDF:**
- [ ] Your name at the top
- [ ] Current title and company
- [ ] Contact information
- [ ] All jobs listed
- [ ] All skills included
- [ ] Projects displayed
- [ ] Education section
- [ ] No text overlapping
- [ ] Professional formatting

---

## Test 6: Verify Resume Data

Check that resume.json loads correctly:

```bash
node -e "
const fs = require('fs');
const resume = JSON.parse(fs.readFileSync('resume.json'));
console.log('Resume Data Check:');
console.log('✅ Name:', resume.personal.name);
console.log('✅ Title:', resume.personal.title);
console.log('✅ Email:', resume.personal.email);
console.log('✅ Location:', resume.personal.location);
console.log('✅ Experience entries:', resume.experience.length);
console.log('✅ Skill categories:', Object.keys(resume.skills).length);
console.log('✅ Skills:', Object.keys(resume.skills).join(', '));
console.log('✅ Projects:', resume.projects.length);
console.log('✅ Education entries:', resume.education.length);
"
```

**Expected output:**
```
Resume Data Check:
✅ Name: Titash Roy Choudhury
✅ Title: Senior Cloud Data Engineer
✅ Email: titash@live.in
✅ Location: Stockholm, Sweden
✅ Experience entries: 6
✅ Skill categories: 8
✅ Skills: cloud, dataEngineering, devOps, ...
✅ Projects: 1
✅ Education entries: 2
```

---

## Test 7: Build Documentation Locally

Test mkdocs (requires Python):

```bash
# Check Python installed
python3 --version

# Install mkdocs if needed
pip3 install mkdocs mkdocs-material

# Build documentation
mkdocs build

# Serve locally (optional)
mkdocs serve
```

**Expected:**
- Documentation site built in `site/` folder
- If serving: Visit http://localhost:8000 to preview

---

## Test 8: Clean Before Deployment

Remove local generated files before pushing:

```bash
# Remove generated PDF
rm Titash_Resume.pdf 2>/dev/null

# Remove built docs (if generated locally)
rm -rf site/ 2>/dev/null

# Verify nothing was deleted in version control
git status
```

**Expected:** Only the files you want to commit show up

---

## Complete Testing Workflow

### For Make Changes to Resume:

```bash
# 1. Edit resume.json
nano resume.json

# 2. Validate JSON
node -e "console.log(JSON.parse(require('fs').readFileSync('resume.json')))" && echo "✅ Valid"

# 3. Generate PDF
npm run generate-pdf

# 4. Review PDF
open Titash_Resume.pdf

# 5. Verify content
node -e "const r = JSON.parse(require('fs').readFileSync('resume.json')); console.log('Entries:', r.experience.length, 'jobs,', r.projects.length, 'projects')"

# 6. Clean up
rm Titash_Resume.pdf

# 7. Commit and push
git add resume.json
git commit -m "Update: Add new experience"
git push origin main
```

---

## Quick Commands Reference

| Task | Command |
|------|---------|
| Install deps | `npm install` |
| Generate PDF | `npm run generate-pdf` |
| Validate JSON | `node -e "JSON.parse(require('fs').readFileSync('resume.json'))"` |
| Build docs | `mkdocs build` |
| Preview docs | `mkdocs serve` |
| Check file size | `ls -lh resume.json` |
| View resume data | `cat resume.json` |
| Git status | `git status` |
| Commit changes | `git add . && git commit -m "msg"` |
| Push to GitHub | `git push origin main` |

---

## Troubleshooting

### ❌ "Cannot find module 'puppeteer'"

```bash
npm install puppeteer
npm run generate-pdf
```

### ❌ "EACCES: permission denied"

```bash
# Fix permissions
chmod -R 755 scripts/
npm run generate-pdf
```

### ❌ "Resume.json: No such file or directory"

```bash
# Make sure you're in the right directory
pwd
ls resume.json
```

### ❌ PDF looks wrong or missing content

- Check JSON is valid
- Verify all required fields exist
- Try after making a small change
- Check script output for errors

### ❌ GitHub Actions failing

- Check GitHub Actions logs at: https://github.com/[username]/[username].github.io/actions
- Look for error messages in the "Generate PDF" step
- Verify resume.json exists and is valid
- Check mkdocs.yml syntax

---

## What to Test After Deployment

Once you deploy to GitHub and it goes live:

### ✅ Visit Your Site

```
https://[username].github.io/
```

Check:
- [ ] Homepage loads
- [ ] Your name displays
- [ ] Download button visible
- [ ] Professional design

### ✅ Download PDF

- Click the download button
- Save the PDF
- Open and review

### ✅ Check Documentation

```
https://[username].github.io/docs/
```

Check:
- [ ] Main documentation page loads
- [ ] Navigation menu works
- [ ] All sections accessible
- [ ] Search function works (if available)
- [ ] Dark mode toggle works (if available)

### ✅ Test Update Process

- Edit resume.json on GitHub directly
- Commit the change
- Watch Actions tab for auto-deployment
- Verify website updates within 2-3 minutes

---

## Performance Tips

### Speed Up Testing

```bash
# Skip validation, go straight to PDF:
npm run generate-pdf 2>/dev/null | grep "✅"

# Quick JSON check:
cat resume.json | wc -l
```

### Optimize PDF Size

If PDF is > 500KB:
- Remove large project images
- Simplify description text
- Check for embedded fonts

---

## Next Steps

Once all tests pass:

1. ✅ Make sure nothing uncommitted
2. ✅ Push to GitHub: `git push origin main`
3. ✅ Check GitHub Actions: https://github.com/[username]/[username].github.io/actions
4. ✅ Visit your live site: `https://[username].github.io/`
5. ✅ Download and review the PDF

See [Quick Reference](./quick-reference.md) for more commands.
