import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data", "matrices")


def load_price_matrices(supplier: str) -> dict:
    """
    Laadt alle prijsmatrices voor een leverancier.
    Verwacht structuur:
    data/matrices/<supplier>/*.xlsx
    """
    supplier = supplier.lower()
    supplier_dir = os.path.join(DATA_DIR, supplier)

    matrices = {}

    if not os.path.isdir(supplier_dir):
        return matrices

    for file in os.listdir(supplier_dir):
        if file.lower().endswith(".xlsx"):
            fabric_name = (
                file.replace("price matrix", "")
                .replace(".xlsx", "")
                .strip()
                .lower()
            )

            path = os.path.join(supplier_dir, file)
            try:
                df = pd.read_excel(path, index_col=0)
                df.index = df.index.astype(float)
                df.columns = df.columns.astype(float)
                matrices[fabric_name] = df
            except Exception as e:
                print(f"❌ Fout bij laden {file}: {e}")

    return matrices
