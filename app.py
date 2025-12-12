import streamlit as st
import pandas as pd
import os

from core.pdf_parser import extract_rows_from_pdf
from core.matrix_loader import load_price_matrices
from core.matcher import evaluate_rows

# ============================================================
# CONFIG
# ============================================================

st.set_page_config(
    page_title="Facturen Checker – TOPPOINT (V2)",
    layout="wide",
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MATRIX_DIR = os.path.join(BASE_DIR, "data", "matrices", "toppoint")

# ============================================================
# UI
# ============================================================

st.title("🔍 Facturen Checker – TOPPOINT (V2)")

uploaded_file = st.file_uploader(
    "Upload verkoopfactuur (PDF)",
    type=["pdf"]
)

# ============================================================
# LOAD MATRICES
# ============================================================

price_matrices = load_price_matrices(MATRIX_DIR)

if not price_matrices:
    st.warning("Nog geen prijsmatrices gevonden.")
else:
    st.success(f"✅ {len(price_matrices)} prijsmatrices geladen")

# ============================================================
# PROCESS PDF
# ============================================================

if uploaded_file and price_matrices:

    with st.spinner("Factuur wordt verwerkt..."):
        rows = extract_rows_from_pdf(uploaded_file)

    if not rows:
        st.error("Geen geldige gordijnregels gevonden in de PDF.")
        st.stop()

    results = evaluate_rows(rows, price_matrices)

    # ========================================================
    # RESULTATEN
    # ========================================================

    st.subheader("Resultaten")

    if results:
        df = pd.DataFrame(results)

        # Mooie volgorde
        df = df[
            [
                "fabric",
                "width",
                "height",
                "price",
                "expected_price",
                "difference",
                "status",
            ]
        ]

        # Afronden
        df["expected_price"] = df["expected_price"].round(2)
        df["difference"] = df["difference"].round(2)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

    else:
        st.info("Geen resultaten om te tonen.")
