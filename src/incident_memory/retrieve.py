from typing import List, Dict

from llama_index.core import StorageContext, load_index_from_storage
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

EMBED_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
PERSIST_DIR = "data/memory_index"

def retrieve_similar_incidents(
    query: str,
    top_k: int = 5,
) -> List[Dict]:
    embed_model = HuggingFaceEmbedding(model_name=EMBED_MODEL_NAME)

    storage_context = StorageContext.from_defaults(
        persist_dir=PERSIST_DIR
        )
    
    index = load_index_from_storage(
        storage_context,
        embed_model=embed_model
        )

    retriever = index.as_retriever(similarity_top_k=top_k)
    results = retriever.retrieve(query)

    return [
        {"incident_id": r.node.metadata["incident_id"], 
        "summary": r.node.text,
        "root_cause": r.node.metadata["root_cause"],
        "score": r.score,
        } for r in results
    ]
