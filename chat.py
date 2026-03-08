import streamlit as st
import os
from io import BytesIO
import google.generativeai as genai
from dotenv import load_dotenv

# ---------------------------------
# Load API Key
# ---------------------------------
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error("GEMINI_API_KEY not found in .env file")
    st.stop()

genai.configure(api_key=API_KEY)

MODEL_NAME = "gemini-2.5-flash"

# ---------------------------------
# Document Parser
# ---------------------------------
try:
    from pypdf import PdfReader
except ImportError:
    PdfReader = None

try:
    from docx import Document
except ImportError:
    Document = None


def read_document_content(uploaded_file):
    ext = os.path.splitext(uploaded_file.name)[1].lower()

    if ext in [".txt", ".md"]:
        return uploaded_file.read().decode("utf-8")

    if ext == ".pdf" and PdfReader:
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text

    if ext == ".docx" and Document:
        doc = Document(BytesIO(uploaded_file.getvalue()))
        return "\n".join(p.text for p in doc.paragraphs)

    return "Error: Unsupported or unreadable file"


# ---------------------------------
# Streamlit UI
# ---------------------------------
st.set_page_config(page_title="Gemini RAG Workshop", layout="wide")
st.title("Gemini RAG – Document Based Q&A")

st.markdown("""
Upload a document and ask questions.  
Gemini will answer **ONLY** from the uploaded document.
""")

# ---------------------------------
# Session State
# ---------------------------------
if "uploaded_text" not in st.session_state:
    st.session_state.uploaded_text = ""

if "answer" not in st.session_state:
    st.session_state.answer = ""

# ---------------------------------
# File Upload
# ---------------------------------
uploaded_file = st.file_uploader(
    "Upload document",
    type=["txt", "md", "pdf", "docx"]
)

if uploaded_file:
    text = read_document_content(uploaded_file)

    if text.startswith("Error"):
        st.error(text)
        st.stop()

    st.session_state.uploaded_text = text
    st.success(f"Loaded {uploaded_file.name} ({len(text)} characters)")

    with st.expander("Preview Document"):
        st.text(text[:2000])

if not st.session_state.uploaded_text:
    st.info("Please upload a document to continue.")
    st.stop()

# ---------------------------------
# Question Input
# ---------------------------------
st.text_area(
    "Ask a question based on the document",
    key="question",
    height=100
)

# ---------------------------------
# RAG Logic
# ---------------------------------
def run_rag():
    question = st.session_state.get("question", "").strip()

    if not question:
        st.error("Please enter a question")
        return

    prompt = f"""
You are a document-based Q&A system.
Answer ONLY from the context below.
If the answer is not present, say:
"I cannot find the answer in the provided document."

Context:
{st.session_state.uploaded_text}

Question:
{question}
"""

    with st.spinner("Generating answer..."):
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(prompt)
        st.session_state.answer = response.text


st.button("Get Grounded Answer", on_click=run_rag, type="primary")

# ---------------------------------
# Output
# ---------------------------------
st.subheader("RAG Response")
st.write(st.session_state.answer)
