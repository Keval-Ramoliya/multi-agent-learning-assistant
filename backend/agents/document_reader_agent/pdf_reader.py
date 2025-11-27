import PyPDF2


def extract_text_from_pdf(path: str) -> str:
    try:
        with open(path, "rb") as f:   # ALWAYS use "rb"
            reader = PyPDF2.PdfReader(f)

            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""

            return text

    except PyPDF2.errors.PdfReadError:
        return "ERROR: Invalid or corrupted PDF file"
    except Exception as e:
        return f"ERROR: {str(e)}"
