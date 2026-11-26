from typing import Any, TypedDict

class SupportWorkflowState(TypedDict, total=False):
    ticket_id: str
    ticket_number: str
    customer_name: str
    customer_email: str
    subject: str
    description: str
    category: str
    priority: str
    sentiment: str
    route: str
    retrieval_query: str
    retrieved_documents: list[dict[str, Any]]
    resolution_recommendation: str
    draft_reply: str
    workflow_status: str
    error: str
