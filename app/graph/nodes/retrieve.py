from app.retrieval.retriever import retrieve_docs


def retrieve_node(state):
    query = state["modified_query"]

    docs = retrieve_docs(query)

    return {
        "retrieve_query": docs
    }