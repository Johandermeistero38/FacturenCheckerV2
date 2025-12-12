import streamlit as st
from core.matrix_loader import load_price_matrices
from core.pdf_parser import extract_rows_from_pdf
from core.matcher import evaluate_rows

st.set_page_config(page_title="Facturen Checker – TOPPOINT (V2)")

st.title("🔍 Facturen Checker – TOPPOINT (V2)")

supplier = "toppoint"

uploaded_file = st.file_uploader(
    "Upload verkoopfactuur (PDF)", type=["pdf"]
)

if uploaded_file:
    rows = extract_rows_from_pdf(uploaded_file)

    matrices = load_price_matrices(supplier)

    if not matrices:
        st.warning("⚠️ Geen prijsmatrices gevonden")
    else:
        st.success(f"✅ {len(matrices)} prijsmatrices geladen")

        results = evaluate_rows(rows, matrices)

        st.subheader("Resultaten")
        st.write(results)
