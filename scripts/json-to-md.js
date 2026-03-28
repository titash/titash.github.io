#!/usr/bin/env node

/**
 * Convert resume.json to professional markdown format
 * Usage: node scripts/json-to-md.js
 * Output: docs/resume.md
 */

const fs = require('fs');
const path = require('path');

const resumeJsonPath = path.join(__dirname, '../resume.json');
const resumeMdPath = path.join(__dirname, '../docs/index.md');

try {
  const resumeData = JSON.parse(fs.readFileSync(resumeJsonPath, 'utf8'));
  
  // Format date helper
  const formatDate = (dateStr) => {
    if (!dateStr) return '';
    const [year, month] = dateStr.split('-');
    const date = new Date(year, parseInt(month) - 1);
    return date.toLocaleDateString('en-US', { year: 'numeric', month: 'short' });
  };

  // Helper to format skill groups
  const skillsHtml = Object.entries(resumeData.skills)
    .map(([key, values]) => {
      const label = key
        .replace(/([A-Z])/g, ' $1')
        .replace(/^./, str => str.toUpperCase())
        .trim();
      return `**${label}:** ${values.join(', ')}`;
    })
    .join('\n\n');

  // Helper to format experience
  const experienceHtml = resumeData.experience
    .map(job => {
      const endDate = job.endDate === 'present' ? 'Present' : formatDate(job.endDate);
      const dateRange = `${formatDate(job.startDate)} – ${endDate}`;
      
      const highlights = job.highlights
        .map(h => `- ${h}`)
        .join('\n');
      
      return `### ${job.role}\n**${job.company}** | ${job.location} | *${dateRange}*\n\n${job.description}\n\n${highlights}`;
    })
    .join('\n\n---\n\n');

  // Helper to format projects
  const projectsHtml = resumeData.projects
    .map(project => {
      const link = project.url ? ` | [View →](${project.url})` : '';
      const tech = `*${project.technologies.join(', ')}*`;
      return `#### ${project.name}\n${tech}${link}\n\n${project.description}`;
    })
    .join('\n\n');

  // Helper to format education
  const educationHtml = resumeData.education
    .map(edu => 
      `- **${edu.degree}** in ${edu.field} — ${edu.institution}, ${edu.location} (${edu.year})`
    )
    .join('\n');

  // Helper to format certifications
  const certificationsHtml = resumeData.certifications && resumeData.certifications.length > 0
    ? resumeData.certifications
        .map(cert => `- **${cert.name}** — ${cert.issuer}`)
        .join('\n')
    : '';

  // Build markdown
  const markdown = `---
title: Resume
description: Professional resume of ${resumeData.personal.name}
---

# ${resumeData.personal.name}

**${resumeData.personal.title}** @ ${resumeData.personal.company}

${resumeData.personal.email} | ${resumeData.personal.phone} | ${resumeData.personal.location} | ${resumeData.personal.visaStatus}

---

## Executive Summary

${resumeData.summary}

---

## Core Competencies

${skillsHtml}

---

## Professional Experience

${experienceHtml}

---

## Featured Projects

${projectsHtml}

---

## Education

${educationHtml}

${certificationsHtml ? `\n---\n\n## Certifications\n\n${certificationsHtml}` : ''}

---

*Last updated: ${new Date().toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })}*
`;

  fs.writeFileSync(resumeMdPath, markdown);
  console.log(`✅ Resume generated: ${resumeMdPath}`);
} catch (error) {
  console.error('❌ Failed to generate resume:', error.message);
  process.exit(1);
}
