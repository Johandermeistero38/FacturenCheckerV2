import pdfplumber


def extract_rows_from_pdf(pdf_file):
    """
    Leest een PDF en geeft ruwe tekstregels terug.
    (We houden dit bewust simpel in V2)
    """
    rows = []

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue
            for line in text.split("\n"):
                rows.append(line.strip())

    return rows
