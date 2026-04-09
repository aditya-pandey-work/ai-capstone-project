
# def chunking(pages, chunk_size=500, overlap=50):
#     chunks = []

#     for page in pages:
#         text = page["text"]

#         start = 0
#         while(start < len(text)):
#             chunk = text[start:start+chunk_size]

#             start = (start+chunk_size)-overlap

#             chunks.append({
#                 "text": chunk, 
#                 "page": page["page"]
#             })


#     return

from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_text(pages):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, 
        chunk_overlap=50
    )

    chunks = []

    for page in pages: 
        texts = splitter.split_text(page["text"])

        for t in texts:
            chunks.append({
                "text": t, 
                "metadata": page["metadata"]
            })
        
    return chunks