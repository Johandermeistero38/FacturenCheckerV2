def evaluate_rows(invoice_rows: list, price_matrices: dict) -> list:
    """
    Vergelijkt factuurregels met prijsmatrices.
    """

    results = []

    for row in invoice_rows:
        fabric = row["fabric"].lower()
        width = row["width"]
        height = row["height"]
        price = row["price"]

        if fabric not in price_matrices:
            results.append({
                **row,
                "expected_price": None,
                "difference": None,
                "status": "❌ Geen matrix"
            })
            continue

        matrix = price_matrices[fabric]

        # Zoek dichtstbijzijnde maat
        matrix["diff"] = (
            (matrix["width"] - width).abs()
            + (matrix["height"] - height).abs()
        )

        best = matrix.sort_values("diff").iloc[0]
        expected = float(best["price"])
        difference = round(price - expected, 2)

        status = "✅ OK" if abs(difference) < 0.5 else "⚠️ Afwijking"

        results.append({
            **row,
            "expected_price": round(expected, 2),
            "difference": difference,
            "status": status
        })

    return results
