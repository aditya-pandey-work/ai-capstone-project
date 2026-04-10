from langchain_core.prompts import ChatPromptTemplate
from app.generation.generator import llm

prompt = ChatPromptTemplate.from_template("""
You are a query rewriting assistant.

Your job is to rewrite ONLY IF needed.

Rules:
- If it contains references like "it", "its", "they", "that" → rewrite it using history, try to answer what does it means by looking at history. 
- Find the value of its and replace it. 
- If the question is already clear and standalone → RETURN IT AS IS
- Do NOT change meaning
- Do NOT convert statements into questions
- Do NOT invent new intent

Chat History:
{history}

User Input:
{question}

Final Output (only the final question, no explanation):
""")

def rewrite_node(state):
    query = state["query"]
    history = state.get("chat_history", [])

    history_text = ""

    last_user_query = ""
    for msg in reversed(history):
        if msg["role"] == "user":
            last_user_query = msg["content"]
            break

    history_text = f"Previous Question: {last_user_query}"

    # for msg in history:
    #     history_text += f"{msg['role']}: {msg['content']}\n"

    chain = prompt | llm 

    response = chain.invoke({
        "history": history_text, 
        "question": query
    })
    # print(response.content.strip())
    print("\n[DEBUG] Rewritten Query:", response.content.strip())

    return {
        "modified_query": response.content.strip()
    }
