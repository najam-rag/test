import streamlit as st
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
import tempfile
import re

# === Load OpenAI API Key from Streamlit secrets ===
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="AS3000 Code Assistant", layout="wide")
st.title("⚡ AS3000 & Standards Code Assistant")
st.caption("Ask code-related questions. Upload your own standard (PDF), such as AS3000, NCC, or SIRs.")

# === Optional Google Drive link ===
st.markdown("[📁 Click here to open your Google Drive folder](https://drive.google.com/drive/folders/1vp64NKAKz6uyE_7G-pxxbL8en2IpuiJb?ths=true)")

# === File Upload Section ===
uploaded_file = st.file_uploader("📎 Upload your own PDF", type="pdf")

if not uploaded_file:
    st.warning("⚠️ Please upload a PDF to proceed.")
    st.stop()

@st.cache_resource
def load_vectorstore(pdf_path: str):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    db = FAISS.from_documents(chunks, embeddings)
    return db.as_retriever()

# === Load uploaded file ===
with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
    tmp_file.write(uploaded_file.read())
    temp_pdf_path = tmp_file.name

retriever = load_vectorstore(temp_pdf_path)
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
        preview = doc.page_content.strip().replace("\\n", " ")[:500]

        # Try to extract clause number from text using regex
        clause_match = re.search(r"(Clause\\s*\\d+(?:\\.\\d+)+)", preview)
        clause_info = clause_match.group(1) if clause_match else "Clause not found"

        st.markdown(f"**📄 Source {i+1} — Page {page}, {clause_info}**")
        st.code(f"{preview}...", language="text")
