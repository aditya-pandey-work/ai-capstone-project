
def input_guard_node(state):

    query = state["query"].lower()

    blocked_patterns = [
        "ignore previous instructions",
        "system prompt",
        "who are you",
        "jailbreak",
        "act as"
    ]

    for pattern in blocked_patterns: 
        if pattern in query:
            return {
                "answer": "this query is not allowed", 
                "blocked": True
            }
        return {
            "blocked": False
        }

