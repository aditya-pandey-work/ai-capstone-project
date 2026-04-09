from chromadb import PersistentClient
import uuid

client = PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="company_docs")

def store_embeddings(chunks):

    for chunk in chunks: 
        collection.add(
            documents=[chunk["text"]], 
            embeddings=[chunk["embedding"]], 
            metadatas=[chunk.get("metadata", {})],
            ids=[str(uuid.uuid4())]
        )