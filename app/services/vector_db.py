from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance

client = QdrantClient("localhost", port=6333)  # or Docker

# Create collection for your embeddings
client.create_collection(
    collection_name="my_documents",
    vectors_config=VectorParams(
        size=embeddings.shape[1], distance=Distance.COSINE
    )
)

# Insert embeddings with metadata
for idx, (vector, sentence) in enumerate(zip(embeddings, all_sentences)):
    payload = {
        "sentence": sentence,
        # add other metadata: document, author, etc. here
    }
    client.upsert(collection_name="my_documents", points=[
        PointStruct(id=idx, vector=vector.tolist(), payload=payload)
    ])
