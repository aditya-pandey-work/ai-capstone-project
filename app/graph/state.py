from typing import TypedDict, List, Dict

class GraphState(TypedDict):
    query: str
    chat_histroy: List[Dict]
    modified_query: str
    retrieve_query: List[Dict]
    answer: str 
    blocked: bool