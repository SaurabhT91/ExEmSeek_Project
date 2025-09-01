def split_text_to_sentences(text: str) -> list[str]:
    sentences = [s.strip() for s in text.split('.') if len(s.strip()) > 0]
    return sentences
