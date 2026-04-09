from typing import TypedDict, List, Dict

class GraphState(TypedDict):
    query: str
    retrieve_query: List[Dict]
    answer: str 