from app.generation.generator import llm
from langchain_core.prompts import ChatPromptTemplate
import re

prompt = ChatPromptTemplate.from_template("""
Check if the answer is grounded in the provided context.

Context:
{context}

Answer:
{answer}

If the answer is NOT supported by context, say "UNSUPPORTED".
Otherwise say "SUPPORTED".""")


def contains_pii(text):

    patterns = [
        r"\b\d{10}\b", 
        r"\S+\.\S+@\S+\.\S+\.\S+"
    ]

    for pattern in patterns:
        if re.search(pattern, text):
            return True
    return False

def output_guard_node(state):
    
    docs = state["retrieve_query"]
    answer = state["answer"]

    context = "\n".join([d["text"] for d in docs])

    chain = prompt | llm

    result = chain.invoke({
        "context": context, 
        "answer": answer
    })

    verdict = result.content.strip()

    if "UNSUPPORTED" in verdict:
        return {
            "answer": "The answer could not be verified from the documents", 
            "blocked": True
        }
    elif contains_pii(answer):
        return {
            "answer": "The output contains confidential information", 
            "blocked": True
        }

    return {
        "blocked": False
    }