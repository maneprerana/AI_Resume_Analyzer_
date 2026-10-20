# 🤖 AI Resume Analyzer & Job Matcher

An AI-powered web application that analyzes resumes against job descriptions, identifies matching skills, highlights potential skill gaps, and provides suggestions to improve a candidate's resume.

## 🚀 Project Overview

Finding the right job can be challenging. This application helps job seekers compare their resumes with job descriptions and understand how well their skills align with a target role.

Users can upload a PDF resume, paste a job description, and receive an analysis with a similarity score, matched skills, potentially missing skills, and improvement suggestions.

## ✨ Features

* 📄 Upload resumes in PDF format
* 📝 Paste a job description for comparison
* 📊 Calculate resume and job description similarity using TF-IDF and cosine similarity
* ✅ Identify matching skills
* 🎯 Highlight potentially missing skills
* 💡 Provide resume improvement suggestions
* 📈 Visualize analysis results with a chart
* 📥 Download a PDF analysis report
* 🌐 Access the application through a web interface

## 🛠️ Technologies Used

* **Python** — Core programming language
* **Streamlit** — Web application interface
* **PyPDF** — PDF text extraction
* **Scikit-learn** — TF-IDF vectorization and cosine similarity
* **Pandas** — Data handling, where applicable
* **Matplotlib** — Data visualization

## ⚙️ How It Works

1. Upload your resume as a PDF file.
2. Paste the job description into the application.
3. The application extracts text from the resume.
4. TF-IDF and cosine similarity are used to estimate textual similarity.
5. The application compares skills against its predefined skill list.
6. Results and improvement suggestions are displayed.
7. Download the analysis report as a PDF.

## 💻 Run the Project Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

### 2. Open the project folder

```bash
cd AI_Resume_Analyzer
```

### 3. Install the dependencies

```bash
pip install streamlit pypdf scikit-learn pandas matplotlib
```

### 4. Run the application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## 🎯 Use Cases

* Job seekers preparing for interviews
* Fresh graduates applying for entry-level positions
* Candidates comparing their resumes with job requirements
* Users identifying skills they may need to develop

## 🔒 Privacy Notice

The application processes uploaded resumes for analysis. When deployed on Streamlit Community Cloud, processing takes place in the cloud environment rather than on the user's own computer. Avoid uploading sensitive personal information.

## ⚠️ Limitations

* The similarity score is a text similarity estimate, not a guarantee of job suitability.
* Skill matching depends on the predefined skill list and may miss relevant skills or equivalent terminology.
* PDF text extraction may not work correctly with scanned or image-only documents.
* Suggestions should be reviewed and tailored to the target job.

## 👩‍💻 Author

**Prerana Mane**

BCA Graduate | Aspiring Data Analyst | AI & Data Science Enthusiast

---

⭐ If you find this project useful, feel free to explore the code and share feedback.
