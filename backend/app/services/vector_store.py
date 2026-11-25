import uuid
from qdrant_client import QdrantClient, models
from app.core.config import settings
from app.services.embeddings import embed_texts

client = QdrantClient(url=settings.qdrant_url, timeout=30)
VECTOR_SIZE = 384

def ensure_collection() -> None:
    if not client.collection_exists(settings.qdrant_collection):
        client.create_collection(
            collection_name=settings.qdrant_collection,
            vectors_config=models.VectorParams(size=VECTOR_SIZE, distance=models.Distance.COSINE),
        )

def index_chunks(document_id: str, filename: str, chunks: list[dict]) -> int:
    ensure_collection()
    vectors = embed_texts([c["text"] for c in chunks])
    points = []
    for chunk, vector in zip(chunks, vectors):
        points.append(models.PointStruct(
            id=str(uuid.uuid4()), vector=vector,
            payload={"document_id": document_id, "filename": filename, "page": chunk.get("page"),
                     "chunk_index": chunk["chunk_index"], "text": chunk["text"]},
        ))
    if points:
        client.upsert(collection_name=settings.qdrant_collection, points=points, wait=True)
    return len(points)

def search(query: str, limit: int = 5) -> list[dict]:
    ensure_collection()
    vector = embed_texts([query])[0]
    hits = client.query_points(collection_name=settings.qdrant_collection, query=vector, limit=limit, with_payload=True).points
    return [{"text": h.payload.get("text", ""), "filename": h.payload.get("filename", "Unknown"),
             "document_id": h.payload.get("document_id"), "page": h.payload.get("page"), "score": h.score}
            for h in hits]

def delete_document(document_id: str) -> None:
    if client.collection_exists(settings.qdrant_collection):
        client.delete(collection_name=settings.qdrant_collection, points_selector=models.FilterSelector(
            filter=models.Filter(must=[models.FieldCondition(key="document_id", match=models.MatchValue(value=document_id))])
        ), wait=True)
