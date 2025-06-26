import streamlit as st
import os
import hashlib
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
import tempfile
import re

# === NEW OCR Libraries ===
from pdf2image import convert_from_path
import pytesseract
from langchain.schema import Document

# ✅ Add password check here
st.sidebar.header("🔐 Login")
password = st.sidebar.text_input("Enter password", type="password")

if password != "yourStrongPassword":
    st.warning("🚫 Access denied. Please enter the correct password.")
    st.stop()

# === Load OpenAI API Key from Streamlit secrets ===
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="Code Assistant", layout="wide")
st.title("⚡ Codes & Standards Assistant")
st.caption("Ask code-related questions. Upload your own standard (PDF), such as AS3000, NCC, or SIRs.")

# === Optional Google Drive link ===
st.markdown("[📁 Click here to open your Google Drive folder](https://drive.google.com/drive/folders/1vp64NKAKz6uyE_7G-pxxbL8en2IpuiJb?ths=true)")

# === File Upload Section ===
uploaded_file = st.file_uploader("📎 Upload your own PDF", type="pdf")

if not uploaded_file:
    st.warning("⚠️ Please upload a PDF to proceed.")
    st.stop()

@st.cache_resource
def load_vectorstore_with_cache(pdf_bytes: bytes):
    pdf_hash = hashlib.md5(pdf_bytes).hexdigest()
    vectorstore_dir = f"vectorstores/{pdf_hash}"
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    db = None
    if os.path.exists(vectorstore_dir):
        try:
            db = FAISS.load_local(vectorstore_dir, embeddings)
        except Exception:
            st.warning("⚠️ Existing vectorstore seems corrupted or incompatible. Rebuilding...")
            os.system(f"rm -rf {vectorstore_dir}")  # Delete corrupted store

    if db is None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(pdf_bytes)
            temp_pdf_path = tmp_file.name

        loader = PyPDFLoader(temp_pdf_path)
        try:
            docs = loader.load()
        except Exception:
            docs = []

        if not docs:
            st.warning("⚠️ No extractable text found. Using OCR to read scanned PDF...")
            images = convert_from_path(temp_pdf_path)
            texts = [pytesseract.image_to_string(img) for img in images]
            docs = [Document(page_content=t, metadata={"page": i + 1}) for i, t in enumerate(texts)]

        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = splitter.split_documents(docs)

        if not chunks:
            raise ValueError("❌ No text could be extracted from the PDF (even with OCR). Please check your file format.")

        # ✅ Better handling (no crash)
        if not chunks:
            st.error("❌ No text could be extracted from the PDF (even with OCR). Please check your file format.")
            st.stop()
     
         # ✅ ADD THIS SAFETY CHECK
        if not chunks:
            raise ValueError("❌ No text could be extracted from the PDF (even with OCR). Please check your file format.")
            st.stop()
      
        db = FAISS.from_documents(chunks, embeddings)
        db.save_local(vectorstore_dir)

    return db.as_retriever()

# === Process uploaded file with caching ===
pdf_bytes = uploaded_file.read()
retriever = load_vectorstore_with_cache(pdf_bytes)
st.success("✅ Custom PDF loaded successfully.")

# === Build QA Chain ===
llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-3.5-turbo")
qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)

# === User Query ===
query = st.text_input("💬 Ask a question:")

if query:
    result = qa({"query": query})
    st.write("### 🔍 Answer")
    st.success(result["result"])

    st.write("### 📚 Source Snippets")
    for i, doc in enumerate(result["source_documents"][:2]):
        page = doc.metadata.get("page", "N/A")
        preview = doc.page_content.strip().replace("\n", " ")[:500]

        # Enhanced clause extraction using multiple regex patterns
        def extract_clause(text):
            patterns = [
                r"(Clause\s*\d{1,2}\.\d{1,2}(?:\.\d{1,2})?)",     # Clause 2.9.4.1
                r"(\d{1,2}\.\d{1,2}(?:\.\d{1,2})?)",              # 2.9.4.1 (no Clause)
                r"(Clause\s*\d{1,2}\.\d{1,2}[a-zA-Z]?)",          # Clause 1.6.2a
                r"(Clause\s*\d{1,2})",                            # Clause 12
            ]
            for pattern in patterns:
                match = re.search(pattern, text)
                if match:
                    return match.group(1)
            return "Clause not found"

        clause_info = extract_clause(preview)

        st.markdown(f"**📄 Source {i+1} — Page {page}, {clause_info}**")
        st.code(f"{preview}...", language="text")
