
def memory_node(state):
    history = state.get('chat_history', [])

    history.append({
        "role": "user",
        "content": state['query']
    })

    history.append({
        "role": "assistant", 
        "content": state['answer']
    })

    history = history[-10:]

    return {
        "chat_history": history
    }