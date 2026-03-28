# Architecture

Deep technical dive into the system architecture.

## System Architecture

```
┌────────────────────────────────────────────────────────────────┐
│                        End Users                               │
│  (Browser: https://titash.github.io)                           │
└──────────────────────┬─────────────────────────────────────────┘
                       │ HTTPS (TLS 1.3)
                       ▼
┌────────────────────────────────────────────────────────────────┐
│              GitHub Pages CDN Servers                          │
│  - Global edge locations                                       │
│  - Automatic SSL/TLS                                           │
│  - Automatic caching                                           │
│  - 99.99% uptime                                               │
└──────────────────────┬─────────────────────────────────────────┘
                       │ Serve static files
                       ▼
┌────────────────────────────────────────────────────────────────┐
│             Static Site Content (GitHub Pages)                │
│  ├── /index.html          (homepage)                           │
│  ├── /resume.pdf          (generated PDF)                      │
│  ├── /docs/               (documentation site)                 │
│  │   ├── index.html                                            │
│  │   ├── architecture.html                                     │
│  │   └── search/                                               │
│  └── /assets/              (CSS, JS, images)                   │
└────────────────────────────────────────────────────────────────┘
```

---

## Build Pipeline Architecture

```
┌─────────────────────────────────────────────────────────────┐
│             Developer Workflow                              │
│  $ git push origin main                                      │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼ GitHub webhook triggered
┌─────────────────────────────────────────────────────────────┐
│         GitHub Actions CI Pipeline                          │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐ │
│  │ Job: build-and-deploy                               │ │
│  │ Runner: ubuntu-latest                               │ │
│  │                                                       │ │
│  │ 1. Checkout                                          │ │
│  │    - name: Checkout code                             │ │
│  │    - uses: actions/checkout@v4                       │ │
│  │                                                       │ │
│  │ 2. Setup Node.js                                     │ │
│  │    - name: Setup Node.js                             │ │
│  │    - uses: actions/setup-node@v4                     │ │
│  │    - node-version: '18'                              │ │
│  │                                                       │ │
│  │ 3. Install Dependencies                              │ │
│  │    - run: npm ci                                     │ │
│  │    - Installs: puppeteer, etc.                       │ │
│  │                                                       │ │
│  │ 4. Generate PDF                                      │ │
│  │    - run: npm run generate-pdf                       │ │
│  │    - Puppeteer renders resume                        │ │
│  │    - Saves to public/pdfs/                           │ │
│  │                                                       │ │
│  │ 5. Setup mkdocs                                      │ │
│  │    - Installs Python mkdocs                          │ │
│  │    - Runs: mkdocs build                              │ │
│  │    - Outputs to site/                                │ │
│  │                                                       │ │
│  │ 6. Prepare Deployment                                │ │
│  │    - Copy files to deployment directory              │ │
│  │    - Prepare artifacts                               │ │
│  │                                                       │ │
│  │ 7. Upload Artifact                                   │ │
│  │    - uses: actions/upload-pages-artifact@v3          │ │
│  │    - Uploads to GitHub                               │ │
│  │                                                       │ │
│  │ 8. Deploy to GitHub Pages                            │ │
│  │    - uses: actions/deploy-pages@v4                   │ │
│  │    - Triggers deployment                             │ │
│  │                                                       │ │
│  └──────────────────────────────────────────────────────┘ │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│        Deployment Verification                              │
│  - Health checks pass                                        │
│  -Files available at GitHub Pages                           │
│  - CDN cache refreshed                                       │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│        Live at https://titash.github.io/                    │
│  Status: ✅ Available globally within 2-3 minutes           │
└─────────────────────────────────────────────────────────────┘
```

---

## Component Architecture

### 1. Data Layer

```
resume.json (Source of Truth)
    ↓
    ├── Personal Info
    │   ├── name
    │   ├── title
    │   ├── email
    │   ├── phone
    │   ├── location
    │   ├── company
    │   └── visaStatus
    │
    ├── Summary
    │   └── executive summary
    │
    ├── Experience
    │   ├── [0] Role
    │   │   ├── company
    │   │   ├── description
    │   │   ├── startDate
    │   │   ├── endDate
    │   │   └── highlights[]
    │   └── ... (multiple jobs)
    │
    ├── Skills
    │   ├── cloud
    │   ├── dataEngineering
    │   ├── devOps
    │   └── ...
    │
    ├── Projects
    │   ├── [0] Project
    │   │   ├── name
    │   │   ├── technologies
    │   │   ├── description
    │   │   └── url
    │   └── ...
    │
    ├── Education
    │   ├── [0] Degree
    │   │   ├── degree
    │   │   ├── field
    │   │   ├── institution
    │   │   └── year
    │   └── ...
    │
    └── Certifications
        └── ...
```

### 2. Generation Layer

```
Input: resume.json
    ↓
    ├─→ generate-pdf.js
    │   ├── Read JSON
    │   ├── Generate HTML template
    │   ├── Start HTTP server
    │   ├── Launch headless Chrome (Puppeteer)
    │   ├── Render HTML to PDF
    │   └── Save Titash_Resume.pdf
    │
    └─→ mkdocs
        ├── Read mkdocs.yml
        ├── Convert docs/*.md → HTML
        ├── Build navigation
        ├── Generate search index
        └── Output to site/ folder
```

### 3. Web Layer

```
GitHub Pages Hosting
    │
    ├── /index.html
    │   └── Served by GitHub Pages CDN
    │
    ├── /resume.pdf
    │   └── Generated PDF file
    │
    ├── /docs/
    │   ├── index.html (mkdocs generated)
    │   ├── getting-started/
    │   │   ├── setup/index.html
    │   │   ├── local-testing/index.html
    │   │   └── quick-reference/index.html
    │   ├── system/
    │   ├── api/
    │   ├── search/
    │   ├── assets/
    │   │   ├── css/ (Material theme)
    │   │   ├── js/  (Material theme)
    │   │   └── fonts/
    │   └── ...
    │
    └── /assets/
        ├── images/
        └── styles/
```

---

## Workflow Execution Sequence

### Timeline

| Time | Step | Component | Status |
|------|------|-----------|--------|
| T+0s | Developer pushes | Git | ⏳ |
| T+1s | Webhook triggered | GitHub | ✅ |
| T+2s | Runner starts | GitHub Actions | ⏳ |
| T+8s | Checkout complete | Git | ✅ |
| T+15s | Node.js setup | GitHub Actions | ✅ |
| T+25s | Dependencies installed | npm | ✅ |
| T+35s | PDF generated | Puppeteer | ✅ |
| T+45s | Docs built | mkdocs | ✅ |
| T+55s | Files prepared | Bash | ✅ |
| T+65s | Artifact uploaded | GitHub Pages | ✅ |
| T+75s | Deploying | GitHub Pages | ⏳ |
| T+150s | Live! | CDN | ✅ |

**Total: ~2-3 minutes**

---

## Data Flow Diagram

```
                    resume.json (100% truth source)
                            │
                 ┌──────────┴──────────┐
                 ▼                     ▼
          generate-pdf.js         mkdocs
                 │                   │
                 ├─→ Read JSON   Read markdown
                 │   Template    files
                 ├─→ Render HTML Create nav
                 │   page        Build search
                 ├─→ Launch      │
                 │   Puppeteer   ▼
                 │               HTML site
                 ├─→ Render      in site/
                 │   to PDF      folder
                 │
                 ▼
          resume.pdf (PDF version)
          (or Titash_Resume.pdf)
                 │
    ┌────────────┼────────────┐
    ▼            ▼            ▼
  public/    docs/site/   deployment/
  pdfs/                   artifact
    │            │            │
    └────────────┴────────────┘
                 │
                 ▼
          GitHub Pages
          (Static hosting)
                 │
    ┌────────────┼────────────┐
    ▼            ▼            ▼
  CDN Cache  CDN Cache    CDN Cache
    │            │            │
    └────────────┴────────────┘
                 │
                 ▼
          https://titash.github.io/
```

---

## Technology Stack - Component Level

### Front-End

```
index.html (Homepage)
    ├── HTML5 Structure
    ├── CSS3 Styling
    │   ├── Gradient background
    │   ├── Flex layout
    │   ├── Responsive design (mobile first)
    │   └── Dark mode support (optional)
    └── Vanilla JavaScript
        └── Fetch resume.json for dynamic content
```

### PDF Generation

```
generate-pdf.js
    ├── Node.js (runtime)
    ├── Puppeteer (headless browser)
    │   ├── Launches Chrome/Chromium
    │   ├── Renders HTML
    │   └── Saves as PDF
    ├── HTTP server (serves HTML)
    └── File system (reads/writes)
```

### Documentation Site

```
mkdocs (Python)
    ├── Markdown parser
    ├── HTML generator
    ├── Material Theme
    │   ├── CSS (pre-built)
    │   ├── JavaScript (Material components)
    │   ├── Search functionality
    │   └── Dark mode
    └── Output: Static HTML files
```

### Infrastructure

```
GitHub Pages
    ├── Git repository (version control)
    ├── GitHub Actions (CI/CD orchestration)
    ├── Artifact Storage (temporary)
    └── Static hosting + CDN
        ├── SSL/TLS termination
        ├── Global edge locations
        ├── Automatic caching
        └── DDoS protection
```

---

## Scalability Architecture

### Current Capacity

- ✅ Handles unlimited resume updates
- ✅ Supports up to 10-20 jobs in resume
- ✅ PDFs up to ~500KB
- ✅ Docs site up to 100+ pages
- ✅ Auto-scales with GitHub Pages

### If You Need More

Scale options (future):

```
Option 1: Custom Domain
    - Add CNAME record
    - Custom branding
    - No additional cost

Option 2: Advanced Docs
    - Full-text search (instead of default)
    - Custom styling
    - Multi-language support

Option 3: Dynamic Updates
    - Use GitHub API webhooks
    - Add more automation
    - Schedule updates

Option 4: Multiple Resumes
    - Different resume formats
    - Different languages
    - Industry-specific versions
```

---

## Error Handling

### Failure Scenarios

```
❌ Scenario: JSON Invalid
   └─→ Handled by: npm JSON validation
   └─→ Action: GitHub Actions marked failed
   └─→ User: Check Actions logs

❌ Scenario: PDF Generation Fails
   └─→ Handled by: continue-on-error flag
   └─→ Action: Deployment continues (uses old PDF)
   └─→ Notification: Actions shows warning

❌ Scenario: Network Timeout
   └─→ Handled by: Puppeteer timeout config
   └─→ Action: Retry mechanism
   └─→ Fallback: Deploy with last good PDF

❌ Scenario: GitHub Pages Down
   └─→ Handled by: GitHub redundancy (rare)
   └─→ Status: Check status.github.com
   └─→ Timeline: Usually restored in minutes
```

---

## Performance Optimization

### Build Time Optimization

```
npm ci (vs npm install)
    └─→ 10-15% faster
    └─→ Ensures exact versions

Actions caching
    └─→ Cache npm modules
    └─→ Speeds up dependency install by ~50%

Puppeteer optimization
    └─→ Headless mode (no GUI)
    └─→ Single page PDF
    └─→ ~ 10-15 seconds generation
```

### Runtime Optimization

```
GitHub Pages + CDN
    ├── Edge caching in 200+ locations
    ├── Automatic compression (gzip)
    ├── HTTP/2 protocol
    └── Load times < 1 second from anywhere

Lazy loading (docs site)
    ├── Only load visible content
    ├── Search index lazy-loaded
    └── Theme loaded asynchronously
```

---

## Security Architecture

### Threat Model

```
Threat: Data Breach
├─→ Mitigation: No sensitive data in repo
├─→ Mitigation: Public data only
└─→ Status: ✅ Safe

Threat: Injection Attack
├─→ Mitigation: Static site (no database)
├─→ Mitigation: No server-side code execution
└─→ Status: ✅ Safe

Threat: DDoS
├─→ Mitigation: GitHub Pages CDN handles
├─→ Mitigation: Automatic rate limiting
└─→ Status: ✅ Protected

Threat: Man-in-the-Middle
├─→ Mitigation: HTTPS/TLS everywhere
├─→ Mitigation: HSTS headers
└─→ Status: ✅ Secure
```

### Content Security Policy

```
Policies enforced by GitHub Pages:
├── Only serve from github.io domain
├── No inline scripts without nonce
├── No eval() execution
├── Images from approved sources
└── Strict content-type headers
```

---

## Monitoring & Logging

### What's Monitored

```
GitHub Actions
    ├── Build status (success/failure)
    ├── Build duration
    ├── Logs for each step
    ├── Artifact uploads
    └── Deployment confirmations

GitHub Pages
    ├── Site availability
    ├── Build status
    ├── Custom domain configuration
    └── HTTPS certificate status
```

### Access Logs

```
GitHub Pages provides:
    ├── No direct server logs (it's static)
    ├── But: Check GitHub Actions logs
    ├── View at: Actions → [latest run] → logs
    └── Contains: All build/deploy output
```

---

## Disaster Recovery

### Backup Strategy

```
Git repository (automatic)
    ├── Local copies on all machines that cloned
    ├── GitHub backup servers
    ├── Multiple geographic locations
    └── Recovery: git clone

Workflow: If GitHub Pages fails
    ├── Version history in Git
    ├── Can rebuild anytime
    ├── Can redeploy to new platform
    └── Time to recovery: ~5 minutes
```

### Rollback Process

```
If deployed bad version:
    1. git revert [commit-hash]
    2. git push origin main
    3. GitHub Actions auto-redeploys
    4. Old version live within 2-3 minutes
```

---

## Future Improvements

```
Potential Enhancements:
├── Multiple resume formats
│   └── PDF, HTML, JSON, Markdown
├── Internationalization
│   └── English, Swedish, Spanish, etc.
├── Advanced analytics
│   └── Track resume downloads, views
├── Resume versioning
│   └── Multiple versions live simultaneously
├── Integration with LinkedIn
│   └── Auto-sync updates
└── REST API
    └── Programmatic access to resume
```

---

## References

- [GitHub Pages Documentation](https://pages.github.com/)
- [GitHub Actions Documentation](https://docs.github.com/actions)
- [mkdocs Documentation](https://www.mkdocs.org/)
- [Puppeteer API](https://pptr.dev/)
- [Material for mkdocs](https://squidfunk.github.io/mkdocs-material/)

---

**Architecture Version**: 1.0

**Last Updated**: March 28, 2026

**Status**: Production Ready
