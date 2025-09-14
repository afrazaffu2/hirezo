import PyPDF2
import docx2txt
import io
import streamlit as st



def extract_text_from_pdf(uploaded_file):
    """Extract text from uploaded PDF"""
    try:
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.read()))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        st.error(f"Error reading PDF {uploaded_file.name}: {e}")
        return None

def extract_text_from_docx(uploaded_file):
    """Extract text from uploaded DOCX"""
    try:
        return docx2txt.process(io.BytesIO(uploaded_file.read()))
    except Exception as e:
        st.error(f"Error reading DOCX {uploaded_file.name}: {e}")
        return None