from app.retrieval.retriever import retrieve_docs


def retrieve_node(state):
    query = state["modified_query"]
    user_role = state["user_role"]

    docs = retrieve_docs(query, user_role=user_role)

    return {
        "retrieve_query": docs
    }