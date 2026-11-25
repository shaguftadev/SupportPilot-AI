# 5-minute portfolio demo

1. **Dashboard (30 sec):** show ticket counts, priority mix, and the seeded support queue.
2. **Ticket workflow (60 sec):** open a ticket; change status/priority; explain persistence in PostgreSQL.
3. **AI analysis (60 sec):** click Analyze. Explain that the model extracts category, sentiment, urgency, summary, and recommended next step.
4. **Reply copilot (45 sec):** generate a customer reply, review/edit it, and emphasize human approval.
5. **Knowledge ingestion (60 sec):** upload a product FAQ PDF/TXT/DOCX; show chunks indexed in Qdrant.
6. **Grounded assistant (60 sec):** ask a policy/product question; show answer and source citations.
7. **Architecture (30 sec):** FastAPI, PostgreSQL, Qdrant, local embeddings, LLM provider abstraction, Docker Compose.

Suggested question: “What is our refund window and what information is required to request a refund?” Upload a policy document containing those facts first.
