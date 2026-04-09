from app.generation.generator import generate_answer


def generator(state):
    query = state["query"]
    retrieve_doc = state["retrieve_query"]

    answer = generate_answer(query, retrieve_doc)

    return {
        "answer": answer
    }