from langgraph.graph import END, START, StateGraph
from app.agents.support_workflow.state import SupportWorkflowState
from app.agents.support_workflow.nodes import triage_ticket, route_ticket, retrieve_billing, retrieve_account, retrieve_technical, retrieve_general, recommend_resolution, draft_customer_reply

def build_support_workflow():
    graph = StateGraph(SupportWorkflowState)
    graph.add_node("triage", triage_ticket)
    graph.add_node("retrieve_billing", retrieve_billing)
    graph.add_node("retrieve_account", retrieve_account)
    graph.add_node("retrieve_technical", retrieve_technical)
    graph.add_node("retrieve_general", retrieve_general)
    graph.add_node("recommend_resolution", recommend_resolution)
    graph.add_node("draft_reply", draft_customer_reply)
    graph.add_edge(START, "triage")
    graph.add_conditional_edges("triage", route_ticket, {"billing":"retrieve_billing", "account":"retrieve_account", "technical":"retrieve_technical", "general":"retrieve_general"})
    for node in ("retrieve_billing", "retrieve_account", "retrieve_technical", "retrieve_general"):
        graph.add_edge(node, "recommend_resolution")
    graph.add_edge("recommend_resolution", "draft_reply")
    graph.add_edge("draft_reply", END)
    return graph.compile()
