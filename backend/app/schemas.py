from pydantic import BaseModel, Field
from typing import Literal

class TicketCreate(BaseModel):
    customer_name: str = Field(min_length=1, max_length=120)
    customer_email: str = Field(min_length=3, max_length=255)
    subject: str = Field(min_length=3, max_length=250)
    description: str = Field(min_length=5)
    priority: Literal["low", "normal", "high", "urgent"] = "normal"

class TicketUpdate(BaseModel):
    status: Literal["open", "in_progress", "waiting", "resolved", "closed"] | None = None
    priority: Literal["low", "normal", "high", "urgent"] | None = None

class ChatRequest(BaseModel):
    question: str = Field(min_length=2, max_length=4000)

class Citation(BaseModel):
    document: str
    page: int | None = None
    snippet: str
    score: float | None = None
