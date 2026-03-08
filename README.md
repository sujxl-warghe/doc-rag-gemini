# 📄 Gemini RAG – Document Based Q&A

A **Retrieval-Augmented Generation (RAG)** application built with **Streamlit + Google Gemini** that allows users to upload documents and ask questions based strictly on the document content.

The AI model will **only answer from the uploaded document** and will refuse to answer if the information is not present.

---

# 🚀 Features

* 📂 Upload documents (`.txt`, `.md`, `.pdf`, `.docx`)
* 🤖 AI powered by **Google Gemini 1.5 Flash**
* 🔍 Question answering **grounded in document content**
* ⚡ Fast and lightweight **Streamlit interface**
* 📑 Document preview before asking questions
* 🛡 Prevents hallucination by restricting answers to document context

---

# 🖥 Demo Workflow

1. Upload a document
2. Preview extracted text
3. Ask a question about the document
4. Gemini generates an answer **based only on that document**

If the answer doesn't exist in the document, the system responds:

```
I cannot find the answer in the provided document.
```

---

# 🛠 Tech Stack

* **Python**
* **Streamlit**
* **Google Gemini API**
* **PyPDF**
* **python-docx**
* **dotenv**

---

# 📂 Project Structure

```
gemini-rag/
│
├── app.py
├── .env
├── requirements.txt
├── README.md
```

---

# ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/gemini-rag.git
cd gemini-rag
```

### 2️⃣ Create virtual environment

```
python -m venv venv
```

Activate it:

Windows

```
venv\Scripts\activate
```

Mac / Linux

```
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

# 🔑 Environment Setup

Create a `.env` file in the project root.

```
GEMINI_API_KEY=your_api_key_here
```

Get your API key from:

https://aistudio.google.com/app/apikey

---

# ▶️ Run the Application

```
streamlit run app.py
```

Then open:

```
http://localhost:8501
```

---

# 📄 Supported File Types

| Format   | Supported |
| -------- | --------- |
| TXT      | ✅         |
| Markdown | ✅         |
| PDF      | ✅         |
| DOCX     | ✅         |

---

# ⚠ Limitations

* Entire document is passed to the model (not chunked)
* Very large files may hit token limits
* Not optimized for large-scale RAG pipelines

---

# 🔮 Future Improvements

* Vector Database (FAISS / Chroma)
* Document chunking
* Semantic search
* Multi-document support
* Streaming responses

---

# 👨‍💻 Author

**Sujal Warghe**

AI Developer | Python | Generative AI | Automation

GitHub:

```
https://github.com/your-username
```

---

# ⭐ Support

If you like this project, consider giving it a **star ⭐ on GitHub**.
