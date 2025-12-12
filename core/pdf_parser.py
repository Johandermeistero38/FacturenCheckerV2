def extract_rows_from_pdf(file) -> list[dict]:
    """
    Simuleert meerdere gordijnregels zoals ze straks uit een echte PDF komen.
    Dit is tijdelijk, puur om de keten stabiel te maken.
    """

    return [
        {
            "fabric": "cosa",
            "width": 140,
            "height": 250,
            "price": 99.00
        },
        {
            "fabric": "voile",
            "width": 200,
            "height": 260,
            "price": 75.00
        },
        {
            "fabric": "between",
            "width": 180,
            "height": 240,
            "price": 89.00
        }
    ]
