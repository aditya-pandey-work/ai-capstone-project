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

Answer ONLY from provided context
If the answer is not present say i don't know.
                                          
Context:
{context}
                                          
Question: 
{question}""")


def format_context(docs):

    context = ""

    for i, doc in enumerate(docs):
        context += f"[{i+1}] {doc["text"]}\n"

    return context


def generate_answer(query, docs):

    context = format_context(docs)

    chain = prompt | llm

    response = chain.invoke({
        "context": context, 
        "question": query
    })

    return response.content
    
