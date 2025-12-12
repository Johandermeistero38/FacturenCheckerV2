import streamlit as st
import pandas as pd
from pathlib import Path

from core.pdf_parser import extract_rows_from_pdf
from core.matrix_loader import load_price_matrices
from core.matcher import evaluate_rows


# =========================================================
# CONFIG
# =========================================================

BASE_DIR = Path(__file__).parent
MATRIX_DIR = BASE_DIR / "data" / "matrices" / "toppoint"

st.set_page_config(
    page_title="Facturen Checker – TOPPOINT (V2)",
    layout="wide"
)


# =========================================================
# UI
# =========================================================

st.title("🔍 Facturen Checker – TOPPOINT (V2)")
st.write("Upload een verkoopfactuur (PDF). Alle gordijnregels worden gecontroleerd.")

uploaded_file = st.file_uploader(
    "Upload verkoopfactuur (PDF)",
    type=["pdf"]
)


# =========================================================
# LOGIC
# =========================================================

if uploaded_file:
    # 1. Lees regels uit PDF
    rows = extract_rows_from_pdf(uploaded_file)

    if not rows:
        st.warning("Geen gordijnregels gevonden in de factuur.")
        st.stop()

    # 2. Laad alle matrices
    price_matrices = load_price_matrices(MATRIX_DIR)

    if not price_matrices:
        st.error("Geen prijsmatrices gevonden.")
        st.stop()

    st.success(f"✅ {len(price_matrices)} prijsmatrices geladen")

    # 3. Vergelijk regels met matrices
    results = evaluate_rows(
        invoice_rows=rows,
        price_matrices=price_matrices
    )

    if not results:
        st.warning("Geen resultaten om te tonen.")
        st.stop()

    # 4. Toon resultaten
    df = pd.DataFrame(results)

    df = df[
        [
            "fabric",
            "quantity",
            "width_mm",
            "height_mm",
            "invoice_unit_price",
            "expected_unit_price",
            "difference",
            "status"
        ]
    ]

    df = df.rename(
        columns={
            "fabric": "stof",
            "quantity": "aantal",
            "width_mm": "breedte (mm)",
            "height_mm": "hoogte (mm)",
            "invoice_unit_price": "factuurprijs p/st",
            "expected_unit_price": "verwachte prijs p/st",
            "difference": "verschil",
            "status": "status"
        }
    )

    st.subheader("Resultaten")
    st.dataframe(df, use_container_width=True)

else:
    st.info("⬆️ Upload een PDF om te starten.")
