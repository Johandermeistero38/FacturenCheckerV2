import streamlit as st
from core.pdf_parser import extract_rows_from_pdf
from core.matrix_loader import load_price_matrices
from core.matcher import evaluate_rows
import os

st.set_page_config(page_title="Facturen Checker V2", layout="wide")
st.title("🔍 Facturen Checker – TOPPOINT (V2)")

# --- Upload ---
pdf = st.file_uploader("Upload verkoopfactuur (PDF)", type="pdf")

# --- Load matrices ---
MATRIX_PATH = "data/matrices/toppoint"

if not os.path.exists(MATRIX_PATH):
    st.warning("Nog geen prijsmatrices gevonden.")
else:
    matrices = load_price_matrices(MATRIX_PATH)
    st.success(f"{len(matrices)} prijsmatrices geladen")

# --- Process ---
if pdf and os.path.exists(MATRIX_PATH):
    rows = extract_rows_from_pdf(pdf)
    st.info(f"{len(rows)} regels uit PDF gehaald")

    results = evaluate_rows(rows, matrices)
    st.write(results)
