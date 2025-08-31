import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path: str) -> str:
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def split_text_to_sentences(text: str) -> list[str]:
    sentences = [s.strip() for s in text.split('.') if len(s.strip()) > 0]
    return sentences
