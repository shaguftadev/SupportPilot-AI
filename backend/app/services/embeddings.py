from functools import lru_cache
from fastembed import TextEmbedding

MODEL_NAME = "BAAI/bge-small-en-v1.5"

@lru_cache(maxsize=1)
def get_model() -> TextEmbedding:
    return TextEmbedding(model_name=MODEL_NAME)

def embed_texts(texts: list[str]) -> list[list[float]]:
    model = get_model()
    return [v.tolist() for v in model.embed(texts)]
