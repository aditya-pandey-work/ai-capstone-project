from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import os 
from dotenv import load_dotenv

load_dotenv()


llm = ChatGroq(
    groq_api_key= os.getenv("GROQ_API"), 
    model_name="llama-3.1-8b-instant", 
    streaming=True
)

prompt = ChatPromptTemplate.from_template("""
You are a helpful internal assistant.

Use the context and history to answer.
If the answer is not present say i don't know.
                                          
History:
{history}
                                          
Context:
{context}
                                          
Question: 
{question}""")


def format_context(docs):

    context = ""

    for i, doc in enumerate(docs):
        context += f"[{i+1}] {doc["text"]}\n"

    return context


def generate_answer(query, docs, history):

    context = format_context(docs)
    
    history_text = ""
    for msg in history: 
        history_text += f"{msg['role']}: {msg['content']}\n"

    chain = prompt | llm

    response = chain.invoke({
        "context": context, 
        "question": query, 
        "history": history_text
    })

    return response.content
    
