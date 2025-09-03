import os
from app.services.pdf_extraction import extract_text_from_pdf
from app.services.epub_extraction import extract_text_from_epub
from app.services.utils import split_text_to_sentences
from app.ml_models.embedding_model import train_tokenizer, get_embeddings

def gather_sentences_from_file_list(file_list):
    sentences = []
    for file in file_list:
        if file['type'] == "pdf":
            raw_text = extract_text_from_pdf(file['path'])
        elif file['type'] == "epub":
            raw_text = extract_text_from_epub(file['path'])
        else:
            continue
        sentences.extend(split_text_to_sentences(raw_text))
    return sentences

def gather_sentences_from_folders(root_folder):
    sentences = []
    for folder in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder)
        if not os.path.isdir(folder_path):
            continue
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if file_name.lower().endswith('.pdf'):
                raw_text = extract_text_from_pdf(file_path)
            elif file_name.lower().endswith('.epub'):
                raw_text = extract_text_from_epub(file_path)
            else:
                continue
            sentences.extend(split_text_to_sentences(raw_text))
    return sentences

if __name__ == "__main__":
    file_list = [
        {"type": "pdf", "path": "doc1.pdf"},
        {"type": "epub", "path": "book1.epub"}
    ]
    root_folder = "books"

    # Gather sentences from file list
    sentences_from_files = gather_sentences_from_file_list(file_list)
    print(f"Loaded {len(sentences_from_files)} sentences from file list.")

    # Gather sentences from all folders
    sentences_from_folders = gather_sentences_from_folders(root_folder)
    print(f"Loaded {len(sentences_from_folders)} sentences from folders.")

    # Combine all for training/embedding
    all_sentences = sentences_from_files + sentences_from_folders
    print(f"Total sentences collected: {len(all_sentences)}")

    # Proceed with tokenizer/model
    if all_sentences:
        train_tokenizer(all_sentences)
        embeddings = get_embeddings(all_sentences)
        print(f"Generated {len(embeddings)} embeddings from {len(all_sentences)} sentences.")
    else:
        print("No sentences found to embed.")