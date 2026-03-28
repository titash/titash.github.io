# 🧪 Local Testing Guide - Resume Generation

Test your resume locally before publishing to GitHub Pages!

---

## Prerequisites

Make sure you're in your repository directory:

```bash
cd ~/path/to/titash.github.io
```

And have Node.js installed:

```bash
node --version  # Should be v18+
npm --version   # Should be v9+
```

---

## ✅ Step 1: Install Dependencies

```bash
npm install
```

This installs:
- ✅ `puppeteer` - For PDF generation
- ✅ Any other dependencies in `package.json`

**Output should show:**
```
added XX packages in Xs
```

---

## ✅ Step 2: Verify Files Exist

Check that all required files are in place:

```bash
# Check resume data
cat resume.json | head -20

# Check PDF script
ls -lh scripts/generate-pdf.js

# Check homepage
ls -lh public/index.html

# Check GitHub Actions workflow
ls -lh .github/workflows/deploy.yml
```

**Expected output:**
```
resume.json                    ~15KB  ✅
scripts/generate-pdf.js        ~20KB  ✅
public/index.html              ~5KB   ✅
.github/workflows/deploy.yml    ~2KB   ✅
```

---

## ✅ Step 3: Test PDF Generation

Generate the PDF locally:

```bash
# Run PDF generation script
npm run generate-pdf
```

**What happens:**
1. Script loads `resume.json`
2. Generates HTML from your data
3. Uses Puppeteer to render as PDF
4. Saves to `resume.pdf` in current directory

**Expected output:**
```
Server running on http://localhost:4000
✅ PDF generated successfully: /path/to/resume.pdf
```

---

## ✅ Step 4: Verify PDF Was Created

```bash
# List the generated PDF
ls -lh resume.pdf

# Check file size (should be 200KB-500KB)
file resume.pdf
```

**Expected:**
```
-rw-r--r-- 1 user group 287K resume.pdf
resume.pdf: PDF document, version 1.4
```

**Open the PDF** to verify it looks good:

```bash
# On macOS
open resume.pdf

# On Linux (if you have a PDF viewer)
xdg-open resume.pdf

# Or download it using your file manager
```

---

## ✅ Step 5: Test Web Server Locally (Optional)

If you want to test the website locally:

```bash
# Start a simple HTTP server
python3 -m http.server 8000

# Or using Node.js
npx http-server -p 8000
```

**Then visit:**
- Homepage: `http://localhost:8000/public/index.html`
- Resume JSON: `http://localhost:8000/resume.json`
- Generated PDF: `http://localhost:8000/resume.pdf`

**Stop the server:**
```bash
Ctrl + C
```

---

## ✅ Step 6: Validate JSON Format

Make sure `resume.json` is valid:

```bash
# Use Node.js to validate
node -e "console.log(JSON.parse(require('fs').readFileSync('resume.json')))" && echo "✅ JSON is valid"
```

**Or use online tool:**
- Go to https://jsonlint.com
- Paste contents of `resume.json`
- Should show: "Valid JSON"

---

## ✅ Step 7: Inspect Generated HTML

The PDF script generates HTML internally. To see it:

```bash
# Add debug output to see generated HTML
node -e "
const fs = require('fs');
const resume = JSON.parse(fs.readFileSync('resume.json'));
console.log('Resume loaded with:');
console.log('- Name:', resume.personal.name);
console.log('- Title:', resume.personal.title);
console.log('- Jobs:', resume.experience.length);
console.log('- Skills:', Object.keys(resume.skills).length);
console.log('- Projects:', resume.projects.length);
"
```

**Expected output:**
```
Resume loaded with:
- Name: Titash Roy Choudhury
- Title: Senior Cloud Data Engineer
- Jobs: 6
- Skills: 8
- Projects: 1
```

---

## 🔍 Testing Checklist

```
✅ Step 1: Dependencies installed (npm install)
✅ Step 2: All files exist
  □ resume.json exists
  □ scripts/generate-pdf.js exists
  □ public/index.html exists
  □ .github/workflows/deploy.yml exists

✅ Step 3: PDF generated without errors
  □ npm run generate-pdf completed successfully
  □ No error messages

✅ Step 4: PDF file created
  □ resume.pdf exists
  □ File size > 100KB
  □ File type is PDF

✅ Step 5: PDF looks good
  □ Opened PDF and reviewed content
  □ Formatting looks correct
  □ All sections present
  □ No missing information

✅ Step 6: JSON is valid
  □ JSON validates without errors
  □ All required fields present
  □ No syntax errors

✅ Step 7: Resume data correct
  □ Name and title correct
  □ Contact info correct
  □ All jobs listed
  □ Skills properly categorized
  □ Projects included
```

---

## 🐛 Troubleshooting Local Tests

### ❌ "npm run generate-pdf" fails

**Error: "Cannot find module 'puppeteer'"**
```bash
# Fix: Install dependencies
npm install
```

**Error: "ENOENT: no such file or directory 'resume.json'"**
```bash
# Fix: Make sure you're in the right directory
pwd  # Should show your repo root
ls resume.json  # Should exist
```

### ❌ PDF file not created

**Check for server errors:**
```bash
# Run with verbose output
npm run generate-pdf 2>&1 | grep -i error
```

**Common causes:**
- Puppeteer installation incomplete: `npm install --force`
- Invalid JSON: Validate at https://jsonlint.com
- Missing resume.json fields: Check all required fields exist

### ❌ PDF looks wrong

**Issues to check:**
- Text cut off? → Check CSS in `scripts/generate-pdf.js`
- Wrong formatting? → Adjust PageFormat (A4, Letter, etc.)
- Missing content? → Verify `resume.json` has all data

**To customize:**
Edit `scripts/generate-pdf.js`:
```javascript
// Find this section and modify:
await page.pdf({
  path: pdfPath,
  format: 'A4',      // Change to 'Letter' if needed
  margin: {
    top: '0.5in',    // Adjust spacing
    right: '0.5in',
    bottom: '0.5in',
    left: '0.5in'
  }
});
```

### ❌ "Page crashed" error

**This means:**
- Browser crashed during PDF generation
- Usually memory issue or invalid HTML

**Fixes:**
```bash
# Try with --force-puppeteer-download
npm install puppeteer --force

# Or check available memory
free -h  # Linux
vm_stat  # macOS
```

---

## ✨ What to Test

### Test 1: PDF Content
Open the generated PDF and check:
- [ ] Header has your name
- [ ] Title and company correct
- [ ] Contact info visible
- [ ] All sections present (summary, experience, skills, projects, education)
- [ ] No text overlapping
- [ ] Formatting is professional
- [ ] Page breaks are clean

### Test 2: Resume Data
Verify in `resume.json`:
- [ ] All jobs have correct dates
- [ ] Achievements are clear and concise
- [ ] Skills are well-organized
- [ ] Projects include links
- [ ] Education info correct

### Test 3: File Structure
Check files are where expected:
```bash
tree -L 3 -I 'node_modules'
```

Should show:
```
.
├── .github/workflows/deploy.yml    ✅
├── scripts/generate-pdf.js          ✅
├── public/
│   ├── index.html                   ✅
│   └── pdfs/
├── resume.json                      ✅
├── package.json                     ✅
└── .nojekyll                        ✅
```

---

## 🚀 After Testing Passes

Once all tests pass locally:

```bash
# Stage changes
git add .

# Commit
git commit -m "chore: Add local testing verification"

# Push to GitHub
git push origin main

# Check GitHub Actions
# Go to: https://github.com/titash/titash.github.io/actions
# Watch the workflow run
# Should complete within 2-3 minutes
```

---

## 📊 Expected Timeline

```
Local Testing:
├─ npm install               ~30 seconds
├─ npm run generate-pdf      ~10 seconds
├─ Review PDF                ~2 minutes
├─ Validate JSON             ~10 seconds
└─ Total                     ~3-4 minutes

After pushing to GitHub:
├─ GitHub Actions triggers   ~5 seconds
├─ Checkout & setup          ~10 seconds
├─ Install deps              ~30 seconds
├─ Generate PDF              ~10 seconds
├─ Deploy                    ~20 seconds
└─ Total                     ~2-3 minutes
```

---

## 💡 Pro Tips

### Tip 1: Keep PDF for comparison
```bash
# Save your local PDF
cp resume.pdf ~/Downloads/resume-local.pdf

# After deployment, compare
diff ~/Downloads/resume-local.pdf /path/to/github/resume.pdf
```

### Tip 2: Test after every change
```bash
# Every time you edit resume.json:
npm run generate-pdf && open resume.pdf
```

### Tip 3: Clean up before pushing
```bash
# Remove local generated files
rm resume.pdf

# They'll be regenerated on GitHub
```

### Tip 4: Version your tests
```bash
# Keep a test log
echo "Tested $(date): PDF generation ✅" >> TEST_LOG.md
git add TEST_LOG.md
```

---

## 🎯 Testing Workflow

```
1. Make changes to resume.json
        ↓
2. npm run generate-pdf (local test)
        ↓
3. open resume.pdf (verify output)
        ↓
4. git add . && git commit && git push
        ↓
5. GitHub Actions auto-tests and deploys
        ↓
6. Visit https://titash.github.io/
        ↓
7. Download and compare PDF
```

---

## ✅ You're Ready!

Local testing helps ensure:
- ✅ No surprised on GitHub
- ✅ PDF generates correctly
- ✅ All content is included
- ✅ Formatting looks professional
- ✅ File structure is correct

**Happy testing!** 🧪

Once you're confident, push to GitHub and watch it auto-deploy! 🚀
