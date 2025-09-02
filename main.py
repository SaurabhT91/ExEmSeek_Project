from app.services.pdf_extraction import extract_text_from_pdf
from app.services.epub_extraction import extract_text_from_epub
from app.services.utils import split_text_to_sentences
from app.ml_models.embedding_model import train_tokenizer, get_embeddings

# Your file list (can mix PDF and ePub paths)
file_list = [
    {"type": "pdf", "path": "doc1.pdf"},
    {"type": "epub", "path": "book1.epub"}
]

all_sentences = []
for file in file_list:
    if file['type'] == "pdf":
        raw_text = extract_text_from_pdf(file['path'])
    elif file['type'] == "epub":
        raw_text = extract_text_from_epub(file['path'])
    else:
        continue
    sentences = split_text_to_sentences(raw_text)
    all_sentences.extend(sentences)

train_tokenizer(all_sentences)
embeddings = get_embeddings(all_sentences)
print(f"Generated {len(embeddings)} embeddings from {len(all_sentences)} sentences.")
