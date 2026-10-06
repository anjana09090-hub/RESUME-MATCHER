# Resume Job Finder

A web app built with Python and Streamlit that reads your resume (PDF) and uses an AI model to suggest job roles that match your skills and experience.

## Features
- Upload your resume as a PDF
- Extracts the text from the resume automatically
- AI suggests the **top 5 job roles** ranked from best to least fit
- Explains **why each role fits**, based on skills in your resume
- Lists **skill gaps** you can work on to become a stronger candidate

## Tech Stack
- Python
- Streamlit (web interface)
- LangChain Community + PyPDF (PDF text extraction)
- Requests (API calls)
- python-dotenv (loads the API key)
- Ollama Cloud API (`gpt-oss:120b-cloud` model)

## How It Works
1. You upload a resume PDF.
2. The app extracts the text from every page.
3. The text is sent to the AI model with a prompt that asks for matching job roles, reasons and skill gaps.
4. The result is shown on the page.

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Resume-Job-Finder.git
   cd Resume-Job-Finder
   ```

2. **Install the libraries**
   ```bash
   pip install streamlit requests python-dotenv langchain-community pypdf
   ```

3. **Add your API key**

   Create a file named `.env` in the project folder and add:
   ```
   OLLAMA_API_KEY=your_api_key_here
   ```
   You can create a key from your Ollama account at ollama.com.

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

## Important Notes
- Never upload your `.env` file or your API key to GitHub. Add `.env` to a `.gitignore` file.
- The PDF must contain selectable text. Scanned image-only PDFs cannot be read.

## Future Improvements
- Support for more file types (DOCX)
- Link suggested roles to live job listings
- Download the results as a PDF
