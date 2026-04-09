# def main():
#     print("Hello from ai-proj-capstone!")


# if __name__ == "__main__":
#     main()


# from app.ingestion.chunking import chunk_text
# from app.ingestion.embed import embed_chunks
# from app.ingestion.extractor import extract_pdf
# from app.ingestion.storage import store_embeddings


# txt = extract_pdf("Employee-Handbook.pdf")
# # print(raw_text[:500])

# # print(txt[:500])

# chunked = chunk_text(txt)
# # print(chunked[:2])
# # print(len(chunked))

# emb = embed_chunks(chunked)

# store_embeddings(emb)
# print("Documents successfully loaded")

# from app.retrieval.retriever import retrieve_docs
# from app.generation.generator import generate_answer

# query = "what is the sick leave policy"

# docs = retrieve_docs(query)

# # for i in res: 
# #     print(i["text"])
# #     print(i["metadata"])

# ans = generate_answer(query, docs)

# print(ans)

from app.graph.builder import build_graph

graph = build_graph()

response = graph.invoke({
    "query": "what is the sick leave policy?"
})

print(response["answer"])