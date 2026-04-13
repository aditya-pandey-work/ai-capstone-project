from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-small-en")
client = PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(name="company_docs")

def retrieve_docs(query, top_k=5, user_role="guest"):

    query_emb = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_emb], 
        n_results=top_k, 
        where={"access_role": user_role}
    )

    documents = []

    for i in range(len(results["documents"][0])):
        documents.append({
            "text": results["documents"][0][i], 
            "metadata": results["metadatas"][0][i]
        })
    return documents