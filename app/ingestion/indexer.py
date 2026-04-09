# from app.ingestion.chunking import chunk_text
# from app.ingestion.embed import embed_chunks
# from app.ingestion.extractor import extract_pdf
# from app.ingestion.filter import clean_text
# from app.ingestion.loader import save_file
# from app.ingestion.storage import store_embeddings


# file = save_file("Employee-Handbook.pdf")
# print(file)

# raw_text = extract_pdf(file)
# print(raw_text[:500])

# txt = clean_text(raw_text)
# print(txt[:500])

# chunked = chunk_text(txt)
# print(chunked[:2])
# print(len(chunked))

# emb = embed_chunks(chunked)

# save = store_embeddings(emb)


from app.ingestion.chunking import chunk_text
from app.ingestion.embed import embed_chunks
from app.ingestion.extractor import extract_pdf
from app.ingestion.storage import store_embeddings


txt = extract_pdf("hr-policy.pdf")
# print(raw_text[:500])

# print(txt[:500])

chunked = chunk_text(txt)
# print(chunked[:2])
# print(len(chunked))

emb = embed_chunks(chunked)

store_embeddings(emb)
print("Documents successfully loaded")


