from app.generation.generator import generate_answer


def generator(state):
    query = state["query"]
    retrieve_doc = state["retrieve_query"]
    history = state.get("chat_history", [])

    answer = generate_answer(query, retrieve_doc, history)

    return {
        "answer": answer
    }