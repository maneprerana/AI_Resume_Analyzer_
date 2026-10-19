import streamlit as st
import pypdf
import re
import io

import matplotlib.pyplot as plt

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("🤖 AI Resume Analyzer & Job Matcher")
st.caption("Analyze your resume, identify skill gaps, and improve job readiness.")
st.divider()

st.sidebar.title("📌 About Project")
st.sidebar.write(
    "This application compares your resume with a job description "
    "and identifies matching and potentially missing skills."
)
st.sidebar.info("Built with Python, Streamlit, Scikit-learn and Matplotlib.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📄 Upload Resume")
    resume_file = st.file_uploader(
        "Choose your resume PDF",
        type=["pdf"]
    )

with col2:
    st.subheader("💼 Job Description")
    job_description = st.text_area(
        "Paste the job description",
        height=220,
        placeholder="Paste the complete job description here..."
    )

skills = [
    "python", "sql", "excel", "power bi", "tableau",
    "pandas", "numpy", "machine learning", "data analysis",
    "data visualization", "statistics", "communication",
    "problem solving", "mysql", "deep learning",
    "artificial intelligence", "scikit-learn", "tensorflow",
    "data cleaning", "database", "dashboard", "reporting"
]

if st.button("🔍 Analyze My Resume", use_container_width=True):

    if resume_file is None:
        st.warning("Please upload your resume PDF.")

    elif not job_description.strip():
        st.warning("Please enter a job description.")

    else:
        try:
            reader = pypdf.PdfReader(resume_file)

            resume_text = " ".join(
                page.extract_text() or ""
                for page in reader.pages
            )

            if not resume_text.strip():
                st.error(
                    "Could not extract text from this PDF. "
                    "Please upload a text-based PDF."
                )

            else:
                # Calculate text similarity
                vectorizer = TfidfVectorizer(stop_words="english")

                vectors = vectorizer.fit_transform(
                    [resume_text, job_description]
                )

                similarity = cosine_similarity(
                    vectors[0:1],
                    vectors[1:2]
                )[0][0]

                score = round(similarity * 100, 2)

                # Identify skills
                resume_lower = resume_text.lower()
                job_lower = job_description.lower()

                required_skills = [
                    skill for skill in skills
                    if re.search(
                        r"\b" + re.escape(skill) + r"\b",
                        job_lower
                    )
                ]

                matched_skills = [
                    skill for skill in required_skills
                    if re.search(
                        r"\b" + re.escape(skill) + r"\b",
                        resume_lower
                    )
                ]

                missing_skills = [
                    skill for skill in required_skills
                    if skill not in matched_skills
                ]

                # Dashboard metrics
                st.divider()
                st.header("📊 Resume Analysis Dashboard")

                m1, m2, m3 = st.columns(3)

                m1.metric("Text Similarity", f"{score}%")
                m2.metric("Matched Skills", len(matched_skills))
                m3.metric("Potential Skill Gaps", len(missing_skills))

                st.progress(min(score / 100, 1.0))

                # Matched skills
                st.subheader("✅ Matched Skills")

                if matched_skills:
                    st.success(" • ".join(matched_skills))
                else:
                    st.info("No matching skills detected.")

                # Missing skills
                st.subheader("🎯 Potentially Missing Skills")

                if missing_skills:
                    st.warning(" • ".join(missing_skills))
                else:
                    st.success("All detected required skills appear in your resume.")

                # FEATURE 1: Skills Chart
                st.divider()
                st.subheader("📈 Skills Comparison Chart")

                chart_labels = ["Matched Skills", "Potential Skill Gaps"]
                chart_values = [len(matched_skills), len(missing_skills)]

                fig, ax = plt.subplots()

                bars = ax.bar(chart_labels, chart_values)

                ax.set_ylabel("Number of Skills")
                ax.set_title("Resume Skills vs Job Requirements")

                for bar in bars:
                    height = bar.get_height()
                    ax.text(
                        bar.get_x() + bar.get_width() / 2,
                        height,
                        str(int(height)),
                        ha="center",
                        va="bottom"
                    )

                st.pyplot(fig)
                plt.close(fig)
                # Job Role Recommendations
                st.divider()
                st.subheader("🎯 Recommended Job Roles")

                role_skills = {
                    "Data Analyst": [
                        "python", "sql", "excel", "power bi",
                        "pandas", "numpy", "data analysis",
                        "data visualization", "statistics"
                    ],
                    "Python Developer": [
                        "python", "sql", "database"
                    ],
                    "Machine Learning Intern": [
                        "python", "machine learning", "pandas",
                        "numpy", "scikit-learn"
                    ],
                    "AI/ML Intern": [
                        "python", "artificial intelligence",
                        "machine learning", "numpy"
                    ],
                    "SQL Developer": [
                        "sql", "mysql", "database"
                    ]
                }

                role_scores = {}

                for role, required in role_skills.items():
                    matched = [
                        skill for skill in required
                        if skill in resume_lower
                    ]

                    role_scores[role] = (
                        round(len(matched) / len(required) * 100)
                    )

                ranked_roles = sorted(
                    role_scores.items(),
                    key=lambda item: item[1],
                    reverse=True
                )

                for role, role_score in ranked_roles[:3]:
                    st.write(f"**{role}**")
                    st.progress(role_score / 100)
                    st.caption(
                        f"{role_score}% of the predefined role keywords "
                        "were found in your resume."
                    )

                st.info(
                    "These are preliminary keyword-based suggestions, "
                    "not a guarantee of job suitability."
                )

                # Suggestions
                st.divider()
                st.subheader("💡 Resume Improvement Suggestions")

                if missing_skills:
                    st.write(
                        "Review the missing skills and include only "
                        "those you genuinely know or have used."
                    )

                if score < 40:
                    st.write(
                        "Tailor your resume summary and project "
                        "descriptions to the target role."
                    )

                st.write(
                    "Describe relevant projects, tools, and genuine "
                    "achievements clearly in your resume."
                )

                # FEATURE 2: Create downloadable PDF report
                st.divider()
                st.subheader("📄 Download Analysis Report")

                pdf_buffer = io.BytesIO()
                pdf = canvas.Canvas(pdf_buffer, pagesize=A4)

                page_width, page_height = A4
                y = page_height - 50

                pdf.setFont("Helvetica-Bold", 18)
                pdf.drawString(45, y, "AI Resume Analysis Report")
                y -= 35

                pdf.setFont("Helvetica", 11)
                pdf.drawString(45, y, f"Text Similarity: {score}%")
                y -= 22

                pdf.drawString(
                    45, y,
                    f"Matched Skills: {len(matched_skills)}"
                )
                y -= 22

                pdf.drawString(
                    45, y,
                    f"Potential Skill Gaps: {len(missing_skills)}"
                )
                y -= 35

                pdf.setFont("Helvetica-Bold", 12)
                pdf.drawString(45, y, "Matched Skills")
                y -= 20

                pdf.setFont("Helvetica", 10)

                matched_text = ", ".join(matched_skills) or "None detected"

                for line_start in range(0, len(matched_text), 85):
                    pdf.drawString(45, y, matched_text[line_start:line_start + 85])
                    y -= 15

                y -= 15
                pdf.setFont("Helvetica-Bold", 12)
                pdf.drawString(45, y, "Potentially Missing Skills")
                y -= 20

                pdf.setFont("Helvetica", 10)

                missing_text = ", ".join(missing_skills) or "None detected"

                for line_start in range(0, len(missing_text), 85):
                    pdf.drawString(45, y, missing_text[line_start:line_start + 85])
                    y -= 15

                y -= 25
                pdf.setFont("Helvetica-Oblique", 9)
                pdf.drawString(
                    45, y,
                    "Note: Text similarity is not a hiring probability "
                    "or a complete measure of your abilities."
                )

                pdf.save()
                pdf_buffer.seek(0)

                st.download_button(
                    label="⬇️ Download PDF Report",
                    data=pdf_buffer.getvalue(),
                    file_name="Resume_Analysis_Report.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )

                with st.expander("ℹ️ How does this analyzer work?"):
                    st.write(
                        "TF-IDF and cosine similarity compare resume text "
                        "with the job description. A predefined keyword list "
                        "is used to identify matching skills and potential gaps."
                    )
                    st.write(
                        "The similarity score is not a hiring probability. "
                        "Skill detection can miss synonyms and context."
                    )

                st.info(
                    "Your resume is processed locally while the app runs "
                    "on your own computer. Avoid deploying it publicly "
                    "without reviewing privacy and security."
                )

        except Exception as error:
            st.error(f"Analysis failed: {error}")