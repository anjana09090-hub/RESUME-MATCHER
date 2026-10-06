import os
import requests
import streamlit as st
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader

st.set_page_config(page_title="Resume Job Finder", page_icon="📄")
st.title("📄 Resume Job Finder")

load_dotenv()
API_KEY = os.getenv("OLLAMA_API_KEY")

if not API_KEY:
    st.error("❌ Missing Ollama API key. Add OLLAMA_API_KEY to your .env file.")
    st.stop()

st.write("Upload your resume and get suggested job roles that fit your skills and experience.")

resume_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
analyze_button = st.button("Find Matching Jobs")

if analyze_button:
    if not resume_file:
        st.warning("Please upload a resume PDF first.")
        st.stop()

    temp_path = "temp_resume.pdf"
    with open(temp_path, "wb") as f:
        f.write(resume_file.getvalue())

    with st.spinner("Reading your resume..."):
        loader = PyPDFLoader(temp_path)
        pages = loader.load()
        resume_text = "\n".join(page.page_content for page in pages)

    os.remove(temp_path)

    if not resume_text.strip():
        st.error("Couldn't extract any text from this PDF. Make sure it's not a scanned image.")
        st.stop()

    prompt = f"""You are an expert career coach and recruiter.

Based on the RESUME below, suggest job roles that best fit this person's skills and experience.

Respond in exactly these sections:

### Top Job Role Matches
List 5 specific job titles that best fit this resume, ranked from best to least fit.

### Why These Fit
For each job title above, give 1-2 sentences on why it fits, based on specific skills/experience from the resume.

### Skill Gaps to Consider
List 3-5 skills that, if added, would make this person a stronger fit for these roles.

RESUME:
{resume_text}
"""

    urls = "https://ollama.com/api/chat"
    header = {
        "Authorization": f"Bearer e77fcafb6a824ea1a2b6e123d43e9050.1Is8bHqFe57DLXWL8sdtA0RK"
    }
    data = {
        "model": "gpt-oss:120b-cloud",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": False
    }

    with st.spinner("Finding matching roles..."):
        try:
            response = requests.post(url=urls, headers=header, json=data, timeout=60)
        except requests.RequestException as e:
            st.error(f"Network error: {e}")
            st.stop()

    if response.status_code != 200:
        st.error(f"API error {response.status_code}: {response.text}")
        st.stop()

    ans = response.json()
    result = ans["message"]["content"]

    st.subheader("Result")
    st.markdown(result)