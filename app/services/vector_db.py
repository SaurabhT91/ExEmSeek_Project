from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance

def insert_embeddings_to_qdrant(
    embeddings,                   # np.ndarray (n_points, dim)
    sentences,                    # list of str
    metadata_list=None,           # optional list of dicts
    collection_name="my_documents",
    host="localhost",
    port=6333
):
    """
    Inserts embeddings and metadata into Qdrant.
    - embeddings: np.ndarray of shape (n, dim)
    - sentences: list[str] corresponding to embeddings
    - metadata_list: optional list[dict], matching sentences
    """
    client = QdrantClient(host=host, port=port)

    # (Re)create the collection with given vector size and metric
    client.recreate_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=embeddings.shape[1], distance=Distance.COSINE)
    )

    # Prepare points with metadata payloads
    points = []
    for idx, (vector, sentence) in enumerate(zip(embeddings, sentences)):
        payload = {"sentence": sentence}
        if metadata_list and len(metadata_list) == len(sentences):
            payload.update(metadata_list[idx])
        points.append(PointStruct(id=idx, vector=vector.tolist(), payload=payload))

    # Upsert all points to Qdrant
    client.upsert(collection_name=collection_name, points=points)
    print(f"Inserted {len(points)} points into Qdrant collection '{collection_name}'.")
    return True
