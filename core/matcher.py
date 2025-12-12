def evaluate_rows(rows, matrices):
    """
    Dummy matcher (V2 startpunt).
    Later breiden we dit uit met maat + plooi logica.
    """
    results = []

    for row in rows:
        results.append({
            "regel": row,
            "status": "Nog niet vergeleken"
        })

    return results
