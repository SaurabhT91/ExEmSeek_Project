from ebooklib import epub

def extract_text_from_epub(epub_path: str) -> str:
    book = epub.read_epub(epub_path)
    text = ""
    for item in book.get_items():
        if item.get_type() == epub.ITEM_DOCUMENT:
            text += item.get_content().decode('utf-8')
    return text
