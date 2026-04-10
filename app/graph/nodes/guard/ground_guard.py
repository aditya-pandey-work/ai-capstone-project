
def grounding_guard_node(state):
    
    docs = state.get("retrieve_query", [])

    if not docs or len(docs) == 0:
        return {
            "answer": "Could not find relevant information in documents",
            "blocked": True
        }

    return {
        "blocked": False
    }