import json
from pathlib import Path
from typing import List

from llama_index.core import Document, VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding


EMBED_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

def load_incidents(path: Path) -> List[dict]:
    incidents = []
    with path.open() as f:
        for line_num, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue  # skip empty lines
            try:
                incidents.append(json.loads(line))
            except json.JSONDecodeError as e:
                raise ValueError(
                    f"Invalid JSON on line {line_num} of {path}"
                ) from e
    return incidents

        # return a list of json objects


def build_and_persist_index(
    incidents_path: str,
    persist_dir: str,
) -> None:
    incidents = load_incidents(Path(incidents_path))

    documents = [
        Document(
            text=inc["summary"],
            metadata={
                "incident_id": inc["incident_id"],
                "root_cause": inc["root_cause"],
                "dimensions": inc["dimensions"],
                "resolution": inc["resolution"],
            }
        ) for inc in incidents
    ]

    embed_model = HuggingFaceEmbedding(model_name=EMBED_MODEL_NAME)

    index = VectorStoreIndex.from_documents(
        documents,
        embed_model=embed_model,
    )

    Path(persist_dir).mkdir(parents=True, exist_ok=True)

    index.storage_context.persist(persist_dir)

    print(f"Incident memory index built and persisted to {persist_dir}")


