

```text
AI_Resume_Analyzer/
│
├── app.py
└── README.md
# AI Resume Analyzer & Job Matcher

## Project Overview
This Python application compares a resume with a job description and identifies matching skills, potential skill gaps, and suitable job roles.

## Features
- Upload resume in PDF format
- Compare resume with a job description
- Calculate text similarity using TF-IDF and cosine similarity
- Identify matched and missing skills
- Display a skills comparison chart
- Download a PDF analysis report
- Recommend potential job roles
- Provide resume improvement suggestions

## Technologies Used
- Python
- Streamlit
- Scikit-learn
- PyPDF
- Matplotlib
- ReportLab

## Installation
Install the required libraries using:

```bash
python -m pip install streamlit pypdf scikit-learn matplotlib reportlab
```

## How to Run
Run this command in the VS Code terminal:

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal.

## How It Works
The application extracts text from a PDF resume using PyPDF. TF-IDF and cosine similarity compare resume text with the job description. Predefined keywords identify matching skills and potential skill gaps. Matplotlib displays a chart, and ReportLab generates a downloadable PDF report.

## Limitations
- The similarity score is not a probability of getting hired.
- Skill matching depends on predefined keywords.
- Job recommendations are keyword-based suggestions, not predictions from a trained AI model.

## Privacy
When run locally, the application processes the resume on your computer. Do not upload personal resumes or sensitive information to a public repository.

## Author
Prerana Mane