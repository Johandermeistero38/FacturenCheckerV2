import pandas as pd
from pathlib import Path


def load_price_matrices(matrix_dir: Path) -> dict:
    """
    Laadt alle Excel prijsmatrices uit een map.
    Bestandsnaam = stofnaam.
    """

    matrices = {}

    if not matrix_dir.exists():
        return matrices

    for file in matrix_dir.glob("*.xlsx"):
        fabric = (
            file.stem
            .replace(" price matrix", "")
            .replace("_", " ")
            .strip()
            .lower()
        )

        try:
            df = pd.read_excel(file)
            matrices[fabric] = df
        except Exception as e:
            print(f"❌ Kon matrix niet laden: {file.name} → {e}")

    return matrices
