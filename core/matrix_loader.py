import os
import pandas as pd


def load_price_matrices(base_path):
    """
    Laadt alle Excel prijsmatrices uit een map.
    Geeft dict terug: {stofnaam: DataFrame}
    """
    matrices = {}

    for file in os.listdir(base_path):
        if not file.lower().endswith(".xlsx"):
            continue

        stofnaam = file.replace(" price matrix.xlsx", "").strip().lower()
        path = os.path.join(base_path, file)

        df = pd.read_excel(path, index_col=0)
        matrices[stofnaam] = df

    return matrices
