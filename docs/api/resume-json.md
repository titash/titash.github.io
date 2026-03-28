# Resume JSON Schema

Complete reference for the resume.json file structure.

## Overview

The `resume.json` file contains all your resume data in a structured JSON format. This becomes the single source of truth for:

- PDF generation
- Website display
- Documentation
- Future integrations

---

## Full Schema

```json
{
  "personal": {
    "name": "string (required)",
    "title": "string (required)",
    "email": "string (required, email format)",
    "phone": "string (required)",
    "location": "string (required, e.g., 'City, Country')",
    "company": "string (required, current company)",
    "visaStatus": "string (optional, e.g., 'Swedish Resident')"
  },
  
  "summary": "string (required, professional summary, 200-500 chars)",
  
  "skills": {
    "skillCategory": ["string", "string"],
    "anotherCategory": ["string", "string"]
  },
  
  "experience": [
    {
      "role": "string (required)",
      "company": "string (required)",
      "location": "string (required)",
      "startDate": "YYYY-MM-DD (required)",
      "endDate": "YYYY-MM-DD or 'present' (required)",
      "description": "string (required, 1-2 sentences)",
      "highlights": ["string", "string"] (required, 3-5 items)
    }
  ],
  
  "projects": [
    {
      "name": "string (required)",
      "technologies": ["string", "string"] (required)",
      "description": "string (required, 1-2 sentences)",
      "url": "string (optional, full URL)"
    }
  ],
  
  "education": [
    {
      "degree": "string (required, e.g., 'MA')",
      "field": "string (required, e.g., 'Computer Science')",
      "institution": "string (required, university name)",
      "location": "string (required, city)",
      "year": "2020 (required, year graduated)"
    }
  ],
  
  "certifications": [
    {
      "name": "string (required)",
      "issuer": "string (required, organization)",
      "year": "2020 (optional)"
    }
  ]
}
```

---

## Detailed Fields

### `personal` Object

Contact and basic information about you.

#### `name` (string, required)

Your full name as it should appear on resume.

```json
"name": "Titash Roy Choudhury"
```

#### `title` (string, required)

Your current job title.

```json
"title": "Senior Cloud Data Engineer"
```

**Guidelines:**
- Current role only
- Use full title
- 2-4 words typically

#### `email` (string, required)

Professional email address.

```json
"email": "titash@live.in"
```

**Guidelines:**
- Use professional email
- Verify it works
- Check spam folder for responses

#### `phone` (string, required)

Professional phone number.

```json
"phone": "+46 70-739 37 85"
```

**Guidelines:**
- Include country code
- Use consistent formatting
- Use format: +[code] [area] [number]

#### `location` (string, required)

Current city and country.

```json
"location": "Stockholm, Sweden"
```

**Guidelines:**
- City and country only
- Use standard format
- No street addresses

#### `company` (string, required)

Current employer.

```json
"company": "SEB"
```

**Guidelines:**
- Current company name
- Shortened version okay (SEB vs SEB Group)
- Matches your latest job in experience

#### `visaStatus` (string, optional)

Visa/citizenship status (helps employers understand work authorization).

```json
"visaStatus": "Swedish Resident"
```

**Examples:**
- "Swedish Resident"
- "Swedish Citizen"
- "Work Permit Valid Until 2025"
- "EU Work Authorization"

---

### `summary` (string, required)

Professional executive summary about your background.

```json
"summary": "Passionate Cloud Data Engineer with 10+ years experience designing and building scalable data infrastructure. Specialized in AWS, ..."
```

**Guidelines:**
- 200-500 characters
- First person (I believe, My focus, etc.) or third person (Experienced in...)
- Highlight key strengths
- Show unique value
- End with current focus

**Writing Tips:**
- Lead with strongest achievement
- Mention years of experience
- Highlight specialties
- Show passion for field
- Keep professional tone

---

### `skills` Object

Technical and soft skills organized by category.

```json
"skills": {
  "cloud": ["AWS", "GCP", "Azure", "Kubernetes"],
  "dataEngineering": ["Apache Spark", "Airflow", "dbt", "Snowflake"],
  "devOps": ["Docker", "Terraform", "Jenkins", "GitHub Actions"],
  "languages": ["Python", "SQL", "Scala", "Bash"],
  "databases": ["PostgreSQL", "MongoDB", "Redis", "Cassandra"],
  "softSkills": ["Leadership", "Mentoring", "Team Building", "Communication"],
  "certifications": ["AWS Solutions Architect", "Kubernetes Administrator"],
  "tools": ["Git", "VS Code", "Jira", "Confluence"]
}
```

**Guidelines:**
- 5-8 skill categories maximum
- 3-8 items per category
- Order by proficiency (strongest first)
- Use exact names of technologies
- Mix hard and soft skills
- Update regularly with new skills

**Category Examples:**
- cloud, devOps, dataEngineering
- languages, databases, tools
- softSkills, frameworks, methodologies
- certifications, platforms, architectures

---

### `experience` Array

Professional work history, most recent first.

```json
"experience": [
  {
    "role": "Senior Cloud Data Engineer",
    "company": "SEB",
    "location": "Stockholm, Sweden",
    "startDate": "2020-06-01",
    "endDate": "present",
    "description": "Led design and implementation of cloud data infrastructure serving 50+ internal services.",
    "highlights": [
      "Designed and deployed Kubernetes infrastructure supporting 500+ daily jobs",
      "Reduced data pipeline latency by 60% through Apache Spark optimization",
      "Mentored team of 5 data engineers on cloud best practices",
      "Implemented automated CI/CD pipelines reducing deployment time by 80%"
    ]
  }
]
```

#### `role` (string, required)

Job title for this position.

```json
"role": "Senior Cloud Data Engineer"
```

#### `company` (string, required)

Company name.

```json
"company": "SEB Bank"
```

#### `location` (string, required)

Work location (city, country).

```json
"location": "Stockholm, Sweden"
```

#### `startDate` (string, required)

Start date in ISO 8601 format: YYYY-MM-DD

```json
"startDate": "2020-06-01"
```

#### `endDate` (string, required)

End date in ISO 8601 format OR the string "present".

```json
"endDate": "present"
```

or

```json
"endDate": "2023-05-31"
```

#### `description` (string, required)

1-2 sentence description of your overall responsibility.

```json
"description": "Led core data infrastructure team building cloud data platforms for internal analytics and ML services."
```

**Guidelines:**
- 1-2 sentences
- Focus on overall contribution
- Use action verbs
- Quantify where possible
- Specific to the role

#### `highlights` (array, required)

3-5 key achievements from this role.

```json
"highlights": [
  "Designed and deployed AWS data lake processing 100 TB+ daily",
  "Reduced ETL runtime by 70% through distributed computing optimization",
  "Established data quality framework used across 15+ teams",
  "Led team of 5 engineers through successful enterprise cloud migration"
]
```

**Guidelines:**
- 3-5 bullet points
- Quantify achievements (30% improvement)
- Show impact (how it matters)
- Use strong action verbs
- Business value focused

**Action Verbs:**
- Led, Designed, Architected, Built, Implemented
- Optimized, Improved, Enhanced, Reduced, Accelerated
- Mentored, Trained, Managed, Directed, Coordinated

---

### `projects` Array

Notable projects you've worked on.

```json
"projects": [
  {
    "name": "Cloud Data Platform Migration",
    "technologies": ["AWS", "Kubernetes", "Terraform", "Apache Spark"],
    "description": "Migrated on-premise data warehouse to cloud, cutting infrastructure costs by 40%.",
    "url": "https://github.com/example/project"
  }
]
```

#### `name` (string, required)

Project name.

```json
"name": "Real-time Analytics Pipeline"
```

#### `technologies` (array, required)

Technologies used (3-5 items).

```json
"technologies": ["Apache Kafka", "Spark Streaming", "AWS Lambda", "Redshift"]
```

#### `description` (string, required)

What the project does and its impact.

```json
"description": "Built real-time event processing pipeline handling 1M+ events/minute with sub-second latency."
```

#### `url` (string, optional)

Link to project (GitHub, demo, documentation).

```json
"url": "https://github.com/username/project"
```

---

### `education` Array

Educational background.

```json
"education": [
  {
    "degree": "MA",
    "field": "Computer Science",
    "institution": "University of Technology",
    "location": "Stockholm, Sweden",
    "year": 2014
  }
]
```

#### `degree` (string, required)

Degree type (BA, MA, Bachelor, Master, etc).

```json
"degree": "Master of Science"
```

or shorthand:

```json
"degree": "MSc"
```

#### `field` (string, required)

Field of study.

```json
"field": "Computer Science"
```

#### `institution` (string, required)

University or school name.

```json
"institution": "Royal Institute of Technology"
```

#### `location` (string, required)

City, country where studied.

```json
"location": "Stockholm, Sweden"
```

#### `year` (number, required)

Graduation year.

```json
"year": 2014
```

---

### `certifications` Array

Professional certifications.

```json
"certifications": [
  {
    "name": "AWS Certified Solution Architect",
    "issuer": "Amazon Web Services",
    "year": 2020
  }
]
```

#### `name` (string, required)

Full certification name.

```json
"name": "Certified Kubernetes Administrator (CKA)"
```

#### `issuer` (string, required)

Organization that issued the cert.

```json
"issuer": "Linux Foundation"
```

#### `year` (number, optional)

Year obtained.

```json
"year": 2022
```

---

## Example Complete File

Here's a complete `resume.json`:

```json
{
  "personal": {
    "name": "Titash Roy Choudhury",
    "title": "Senior Cloud Data Engineer",
    "email": "titash@live.in",
    "phone": "+46 70-739 37 85",
    "location": "Stockholm, Sweden",
    "company": "SEB",
    "visaStatus": "Swedish Resident"
  },
  
  "summary": "Cloud Data Engineer with 10+ years building scalable data platforms. Expertise in AWS, Kubernetes, and Apache Spark. Passionate about optimizing data pipelines and mentoring engineering teams.",
  
  "skills": {
    "cloud": ["AWS", "Azure", "GCP", "Kubernetes"],
    "dataEngineering": ["Apache Spark", "Airflow", "dbt", "Snowflake"],
    "languages": ["Python", "SQL", "Scala"],
    "devOps": ["Docker", "Terraform", "GitHub Actions"],
    "databases": ["PostgreSQL", "MongoDB", "Redis"],
    "softSkills": ["Leadership", "Mentoring", "Communication"]
  },
  
  "experience": [
    {
      "role": "Senior Cloud Data Engineer",
      "company": "SEB",
      "location": "Stockholm, Sweden",
      "startDate": "2020-06-01",
      "endDate": "present",
      "description": "Leading data infrastructure team building cloud data platforms for enterprise analytics.",
      "highlights": [
        "Designed and deployed Kubernetes infrastructure for 500+ daily data jobs",
        "Reduced ETL latency by 60% through Apache Spark optimization",
        "Mentored 5 team members on cloud data architecture",
        "Implemented automated CI/CD pipeline reducing deployment time 80%"
      ]
    },
    {
      "role": "Data Engineer",
      "company": "Spotify",
      "location": "Stockholm, Sweden",
      "startDate": "2018-03-01",
      "endDate": "2020-05-31",
      "description": "Built data pipelines processing billions of streaming events daily.",
      "highlights": [
        "Designed real-time event pipeline handling 1M+ events/minute",
        "Optimized Spark jobs reducing infrastructure costs by 35%",
        "Led migration from on-premise Hadoop to AWS EMR"
      ]
    }
  ],
  
  "projects": [
    {
      "name": "Cloud Data Platform Migration",
      "technologies": ["AWS", "Kubernetes", "Terraform", "Apache Spark"],
      "description": "Migrated on-premise data warehouse to AWS, cutting infrastructure costs 40% while improving performance.",
      "url": "https://github.com/example"
    }
  ],
  
  "education": [
    {
      "degree": "Master of Science",
      "field": "Computer Science",
      "institution": "Royal Institute of Technology",
      "location": "Stockholm, Sweden",
      "year": 2014
    }
  ],
  
  "certifications": [
    {
      "name": "AWS Certified Solutions Architect",
      "issuer": "Amazon Web Services",
      "year": 2021
    }
  ]
}
```

---

## Validation Rules

### Required Fields

**Always required:**
- personal.name, personal.title, personal.email, personal.phone, personal.location, personal.company
- summary
- experience (at least 1)
- education (at least 1)

### Date Formats

**Use ISO 8601 format:**
- ✅ Correct: `"2020-06-15"`
- ❌ Wrong: `"June 15, 2020"`
- ❌ Wrong: `"15/06/2020"`

### Arrays

**arrays must have at least 1 item:**
- skills: 5-8 categories recommended
- experience: 1+ entries
- highlights: 3-5 entries recommended
- education: 1+ entry

### Strings

**No special formatting needed:**
- Just plain text
- Markdown not supported in JSON
- Keep names consistent across sections

---

## Validation Tools

### Validate Locally

```bash
# Quick validation
node -e "JSON.parse(require('fs').readFileSync('resume.json'))" && echo "✅ Valid"
```

### Online Tools

- [jsonlint.com](https://jsonlint.com) - Copy & paste your resume.json
- [json5.org](https://json5.org/) - Alternative validator

### Visual Editors

- **VS Code** - Built-in JSON validation
- **JSON formatter extensions** - Syntax highlighting

---

## Tips & Best Practices

### Content Tips

✅ **Do:**
- Keep descriptions concise (1-2 sentences)
- Use specific numbers and metrics
- Focus on business impact
- Update regularly
- Use consistent formatting
- 3-5 highlights per job

❌ **Don't:**
- Use personal pronouns (I, you)
- Repeat information
- Use vague descriptions
- Include salary expectations
- List every task/responsibility
- Format with markdown in JSON

### Organization Tips

- List experience most recent first
- Order skills by proficiency
- Include both hard and soft skills
- Update as you gain new experience
- Keep descriptions 1-2 sentences max
- Use strong action verbs

### Formulating Achievements

**Formula:** Action + Metric + Impact

```
❌ Bad: "Worked on data pipeline"
✅ Good: "Optimized data pipeline reducing latency by 60%"

❌ Bad: "Led team"
✅ Good: "Mentored team of 5 engineers on cloud architecture"

❌ Bad: "Implemented system"
✅ Good: "Designed Kubernetes infrastructure supporting 500+ daily jobs"
```

---

## Evolution & Updates

Your resume grows over time:

```
Month 1 (Initial)
└── Create resume.json with current experience

Month 3-6 (Growing)
└── Add completed projects
└── Update with new certifications
└── Refine descriptions based on feedback

Month 12 (Mature)
└── Add recent work achievements
└── Update skills gained
└── Refine for target roles
```

---

## Versioning

Keep historical versions if needed:

```
resume.json              (current)
resume.backup.json       (backup)
resume-2024-03-28.json   (archive)
```

To save version:
```bash
cp resume.json "resume-$(date +%Y-%m-%d).json"
```

---

## Examples by Industry

### Cloud Engineer Focus

```json
"skills": {
  "cloud": ["AWS", "Azure", "Google Cloud"],
  "kubernetes": ["EKS", "AKS", "GKE", "Helm"],
  "devOps": ["Docker", "Terraform", "CI/CD"],
  "languages": ["Python", "Go", "Bash"]
}
```

### Data Engineer Focus

```json
"skills": {
  "dataProcessing": ["Apache Spark", "Flink", "Presto"],
  "orchestration": ["Airflow", "Dagster", "prefect"],
  "dataWarehousing": ["Snowflake", "Redshift", "BigQuery"],
  "languages": ["Python", "SQL", "Scala"]
}
```

### Full Stack Focus

```json
"skills": {
  "backend": ["Python", "Node.js", "Go"],
  "frontend": ["React", "Vue", "Angular"],
  "devOps": ["Docker", "Kubernetes", "AWS"],
  "databases": ["PostgreSQL", "MongoDB", "Redis"]
}
```

---

## API Reference

If integrating with other systems:

```javascript
// JavaScript example
const resume = JSON.parse(fs.readFileSync('resume.json'));

// Access data
console.log(resume.personal.name);        // String
console.log(resume.experience.length);   // Number
console.log(resume.skills.cloud[0]);     // String from array

// Iterate
resume.experience.forEach(job => {
  console.log(`${job.role} at ${job.company}`);
});
```

---

## Support & Questions

- Check examples above
- Validate with jsonlint.com
- Review sample resume.json in your repo
- See [Setup Guide](../getting-started/setup.md) for more info

---

**Schema Version**: 1.0

**Last Updated**: March 28, 2026

**Status**: Production Ready

**Compatible with**: Puppeteer PDF generation, mkdocs documentation, GitHub Pages hosting
