def evaluate_rows(rows: list, price_matrices: dict) -> list:
    """
    Vergelijkt factuurregels met prijsmatrices
    """
    results = []

    for row in rows:
        fabric = row.get("fabric", "").lower()
        width = row.get("width")
        height = row.get("height")
        invoice_price = row.get("price")

        matrix = price_matrices.get(fabric)

        if matrix is None:
            row["status"] = "❌ Geen prijsmatrix"
            results.append(row)
            continue

        try:
            expected_price = matrix.loc[height, width]
            row["expected_price"] = expected_price
            row["difference"] = invoice_price - expected_price
            row["status"] = "✅ OK" if row["difference"] == 0 else "⚠️ Afwijking"
        except Exception:
            row["status"] = "❌ Maat niet gevonden"

        results.append(row)

    return results
