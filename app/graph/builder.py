from langgraph.graph import StateGraph, END
from app.graph.state import GraphState
from app.graph.nodes.retrieve import retrieve_node
from app.graph.nodes.generator import generator


def build_graph():

    graph = StateGraph(GraphState)

    graph.add_node("retriever", retrieve_node)
    graph.add_node("generate", generator)

    graph.set_entry_point("retriever")

    graph.add_edge("retriever", "generate")
    graph.add_edge("generate", END)

    return graph.compile()