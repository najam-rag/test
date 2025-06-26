import streamlit as st
import tempfile
import pytesseract
from fpdf import FPDF
import fitz  # PyMuPDF
from PIL import Image
import io

st.set_page_config(page_title="🧾 OCR PDF Converter", layout="wide")
st.title("🧾 Convert Scanned Image-PDF to OCR-Readable PDF")

uploaded_file = st.file_uploader("📎 Upload an image-based PDF to convert to OCR text PDF", type="pdf")

def extract_images_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    images = []

    for page_index in range(len(doc)):
        pix = doc.load_page(page_index).get_pixmap(dpi=300)
        img_data = pix.tobytes("png")
        img = Image.open(io.BytesIO(img_data))
        images.append(img)

    return images

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_pdf:
        tmp_pdf.write(uploaded_file.read())
        temp_pdf_path = tmp_pdf.name

    st.info("📸 Converting pages to images using PyMuPDF...")
    images = extract_images_from_pdf(temp_pdf_path)

    st.info("🔍 Performing OCR using Tesseract...")
    texts = [pytesseract.image_to_string(img) for img in images]

    st.info("📄 Generating OCR PDF...")
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    for text in texts:
        pdf.add_page()
        pdf.set_font("Arial", size=11)
        for line in text.split('\n'):
            if line.strip():
                pdf.cell(200, 10, txt=line.strip(), ln=True)

    ocr_pdf_path = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf").name
    pdf.output(ocr_pdf_path)

    with open(ocr_pdf_path, "rb") as f:
        st.download_button("⬇️ Download OCR PDF", f.read(), file_name="ocr_output.pdf", mime="application/pdf")

    st.success("✅ OCR conversion completed!")
