from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-small-en")


def embed_chunks(chunks):
    text = [c["text"] for c in chunks]

    embeddings = model.encode(text)

    for i, emb in enumerate(embeddings):
        chunks[i]["embedding"] = emb.tolist()
    
    return chunks