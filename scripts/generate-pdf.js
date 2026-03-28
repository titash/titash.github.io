/**
 * PDF Generation Script
 * Generates PDF from resume.json using Puppeteer
 * Run: node scripts/generate-pdf.js
 */

const puppeteer = require('puppeteer');
const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = 4000;
const RESUME_HTML_PATH = path.join(__dirname, '../public', 'resume.html');
const PDF_OUTPUT_PATH = path.join(__dirname, '../public/pdfs');

// Create simple HTTP server to serve the resume
function startServer() {
  return new Promise((resolve) => {
    const server = http.createServer((req, res) => {
      if (req.url === '/resume' || req.url === '/resume.html') {
        // Generate HTML from JSON resume
        const resumeData = JSON.parse(
          fs.readFileSync(path.join(__dirname, '../resume.json'), 'utf8')
        );
        const html = generateResumeHTML(resumeData);
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(html);
      } else {
        res.writeHead(404);
        res.end('Not found');
      }
    });

    server.listen(PORT, () => {
      console.log(`Server running on http://localhost:${PORT}`);
      resolve(server);
    });
  });
}

// Generate HTML from resume JSON
function generateResumeHTML(data) {
  const skills = Object.entries(data.skills)
    .map(([key, values]) => 
      `<div class="skill-group">
        <strong>${formatKey(key)}:</strong> ${values.join(' • ')}
      </div>`
    )
    .join('');

  const experience = data.experience
    .map(job => 
      `<div class="job">
        <div class="job-header">
          <h3>${job.role}</h3>
          <span class="job-date">${formatDate(job.startDate)} – ${job.endDate === 'present' ? 'Present' : formatDate(job.endDate)}</span>
        </div>
        <div class="job-company">${job.company}, ${job.location}</div>
        <p>${job.description}</p>
        <ul>
          ${job.highlights.map(h => `<li>${h}</li>`).join('')}
        </ul>
      </div>`
    )
    .join('');

  const projects = data.projects
    .map(project => 
      `<div class="project">
        <h4>${project.name}</h4>
        <p class="tech">Technologies: ${project.technologies.join(', ')}</p>
        <p>${project.description}</p>
        ${project.url ? `<p><a href="${project.url}" target="_blank">View Project →</a></p>` : ''}
      </div>`
    )
    .join('');

  return `
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${data.personal.name} - Resume</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }
    
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
      line-height: 1.6;
      color: #333;
      background: white;
      padding: 40px 20px;
    }
    
    .container {
      max-width: 900px;
      margin: 0 auto;
      background: white;
    }
    
    .header {
      border-bottom: 3px solid #0066cc;
      margin-bottom: 30px;
      padding-bottom: 20px;
    }
    
    .name {
      font-size: 32px;
      font-weight: bold;
      color: #000;
      margin-bottom: 5px;
    }
    
    .title {
      font-size: 18px;
      color: #0066cc;
      margin-bottom: 10px;
    }
    
    .contact {
      font-size: 12px;
      color: #666;
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 10px;
      margin-top: 10px;
    }
    
    .contact-item {
      display: flex;
      align-items: center;
      gap: 5px;
    }
    
    h2 {
      font-size: 16px;
      font-weight: bold;
      color: #000;
      border-bottom: 2px solid #0066cc;
      padding-bottom: 8px;
      margin: 25px 0 15px 0;
      text-transform: uppercase;
      letter-spacing: 1px;
    }
    
    h3 {
      font-size: 14px;
      font-weight: bold;
      color: #000;
      margin: 12px 0 4px 0;
    }
    
    h4 {
      font-size: 13px;
      font-weight: bold;
      color: #0066cc;
      margin: 10px 0 3px 0;
    }
    
    .summary {
      font-size: 13px;
      line-height: 1.6;
      color: #555;
      margin-bottom: 10px;
    }
    
    .skills-container {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
      margin-bottom: 10px;
    }
    
    .skill-group {
      font-size: 12px;
      line-height: 1.5;
      padding: 8px;
      background: #f5f5f5;
      border-radius: 4px;
    }
    
    .skill-group strong {
      color: #0066cc;
    }
    
    .job {
      margin-bottom: 18px;
      page-break-inside: avoid;
    }
    
    .job-header {
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      margin-bottom: 3px;
    }
    
    .job-date {
      font-size: 11px;
      color: #999;
      white-space: nowrap;
      margin-left: 10px;
    }
    
    .job-company {
      font-size: 12px;
      color: #666;
      margin-bottom: 5px;
    }
    
    .job > p {
      font-size: 12px;
      margin-bottom: 6px;
      color: #555;
    }
    
    .job ul {
      margin-left: 20px;
      font-size: 12px;
      color: #555;
    }
    
    .job ul li {
      margin-bottom: 3px;
      line-height: 1.4;
    }
    
    .project {
      margin-bottom: 15px;
      page-break-inside: avoid;
    }
    
    .project p {
      font-size: 12px;
      margin-bottom: 4px;
      color: #555;
    }
    
    .tech {
      color: #999;
      font-size: 11px !important;
    }
    
    .project a {
      color: #0066cc;
      text-decoration: none;
    }
    
    .education, .certification {
      font-size: 12px;
      margin-bottom: 8px;
      color: #555;
    }
    
    .education-degree, .certification-name {
      font-weight: bold;
      color: #000;
    }
    
    @media print {
      body {
        padding: 0;
      }
      
      .container {
        max-width: 100%;
      }
    }
    
    @page {
      margin: 0.5in;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <div class="name">${data.personal.name}</div>
      <div class="title">${data.personal.title} @ ${data.personal.company}</div>
      <div class="contact">
        <div class="contact-item">📧 ${data.personal.email}</div>
        <div class="contact-item">📱 ${data.personal.phone}</div>
        <div class="contact-item">📍 ${data.personal.location}</div>
        <div class="contact-item">🇸🇪 ${data.personal.visaStatus}</div>
      </div>
    </div>
    
    <h2>Executive Summary</h2>
    <p class="summary">${data.summary}</p>
    
    <h2>Core Competencies</h2>
    <div class="skills-container">${skills}</div>
    
    <h2>Professional Experience</h2>
    ${experience}
    
    <h2>Featured Projects</h2>
    ${projects}
    
    <h2>Education</h2>
    ${data.education.map(edu => {
      return '<div class="education">' +
        '<span class="education-degree">' + edu.degree + ' in ' + edu.field + '</span><br/>' +
        edu.institution + ', ' + edu.location + ' (' + edu.year + ')' +
        '</div>';
    }).join('')}
    
    ${data.certifications && data.certifications.length > 0 ? 
      '<h2>Certifications</h2>' +
      data.certifications.map(cert => {
        return '<div class="certification">' +
          '<span class="certification-name">' + cert.name + '</span> - ' + cert.issuer +
          '</div>';
      }).join('')
    : ''}
  </div>
</body>
</html>
  `;
}

function formatKey(key) {
  return key.replace(/([A-Z])/g, ' $1').replace(/^./, str => str.toUpperCase()).trim();
}

function formatDate(dateStr) {
  const [year, month] = dateStr.split('-');
  const date = new Date(year, parseInt(month) - 1);
  return date.toLocaleDateString('en-US', { year: 'numeric', month: 'short' });
}

// Generate PDF
async function generatePDF() {
  const server = await startServer();
  
  try {
    const browser = await puppeteer.launch({
      headless: 'new',
      args: ['--no-sandbox', '--disable-setuid-sandbox']
    });

    const page = await browser.newPage();
    await page.goto(`http://localhost:${PORT}/resume`, { waitUntil: 'networkidle2' });
    
    // Ensure output directory exists
    if (!fs.existsSync(PDF_OUTPUT_PATH)) {
      fs.mkdirSync(PDF_OUTPUT_PATH, { recursive: true });
    }
    
    const pdfPath = path.join(PDF_OUTPUT_PATH, 'Titash_Resume.pdf');
    await page.pdf({
      path: pdfPath,
      format: 'A4',
      margin: {
        top: '0.5in',
        right: '0.5in',
        bottom: '0.5in',
        left: '0.5in'
      },
      printBackground: true
    });

    console.log(`✅ PDF generated successfully: ${pdfPath}`);
    
    await browser.close();
    server.close();
  } catch (error) {
    console.error('❌ PDF generation failed:', error);
    server.close();
    process.exit(1);
  }
}

// Run if called directly
if (require.main === module) {
  generatePDF().catch(err => {
    console.error('Fatal error:', err);
    process.exit(1);
  });
}

module.exports = { generatePDF };
