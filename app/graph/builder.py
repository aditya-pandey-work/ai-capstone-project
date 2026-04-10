from langgraph.graph import StateGraph, END
from app.graph.state import GraphState
from app.graph.nodes.rewrite import rewrite_node
from app.graph.nodes.memory import memory_node
from app.graph.nodes.retrieve import retrieve_node
from app.graph.nodes.generator import generator
from app.graph.nodes.guard.input_guard import input_guard_node
from app.graph.nodes.guard.ground_guard import grounding_guard_node
from app.graph.nodes.guard.output_guard import output_guard_node


def should_continue(state):
    return not state.get("blocked", False)


def build_graph():

    graph = StateGraph(GraphState)

    graph.add_node("retriever", retrieve_node)
    graph.add_node("generate", generator)
    graph.add_node("rewrite", rewrite_node)
    graph.add_node("memory", memory_node)
    graph.add_node("input_guard", input_guard_node)
    graph.add_node("grounded_guard", grounding_guard_node)
    graph.add_node("output_guard", output_guard_node)

    graph.set_entry_point("input_guard")

    graph.add_conditional_edges("input_guard", should_continue, {
        True: "rewrite", 
        False: END
    })

    graph.add_edge("rewrite", "retriever")
    graph.add_edge("retriever", "grounded_guard")
    graph.add_conditional_edges("grounded_guard", should_continue, {
        True: "generate", 
        False: END
    })
    graph.add_edge("generate", "output_guard")
    graph.add_conditional_edges("output_guard", should_continue, {
        True: "memory", 
        False: END
    })

    graph.add_edge("memory", END)

    return graph.compile()