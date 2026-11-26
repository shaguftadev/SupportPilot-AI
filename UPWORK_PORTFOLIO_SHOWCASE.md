# SupportPilot AI — Upwork Portfolio Showcase

## Recommended 3–4 minute walkthrough

1. **Dashboard (20–30 sec):** Point out the demo workspace, 600-ticket dataset, queue totals, priority/category distributions, and resolution snapshot. Explain that displayed analytics are calculated from the seeded dataset.
2. **Ticket detail (30 sec):** Open a billing or technical ticket. Show customer context, status, priority, and conversation history.
3. **AI triage (30 sec):** Run analysis and show category, priority, sentiment, and summary.
4. **Agent workflow (45–60 sec):** Run the LangGraph workflow. Explain triage → route → knowledge retrieval → recommendation → reply draft. Open sources and explain grounding/citations.
5. **Human-in-the-loop (45–60 sec):** Reject with specific feedback, show revised recommendation, then approve. Emphasize that approval is required and email sending is a separate explicit action.
6. **Knowledge assistant (20–30 sec):** Ask a question answerable from the uploaded knowledge base and show citations. Ask an unsupported question to demonstrate abstention/uncertainty behavior if working in the current build.
7. **Close (10 sec):** Summarize stack and business value: reduce repetitive support work while keeping a human in control.

## Suggested voiceover

“SupportPilot AI is an AI-assisted customer support workspace I built with React, TypeScript, FastAPI, PostgreSQL, Qdrant, embeddings, and LangGraph. It uses a realistic demo dataset of support tickets. The system analyzes tickets, routes them, retrieves relevant company knowledge, and prepares resolution recommendations and customer replies. The workflow includes human review: a support agent can reject with feedback, request a revision, and approve the result. Sending an email is a separate explicit action, so the AI does not send customer communications automatically. The project demonstrates RAG, agent orchestration, persisted workflows, and human oversight in a practical support use case.”

## Screenshot checklist

- [ ] Dashboard with KPI cards and analytics
- [ ] Ticket list with realistic customer tickets
- [ ] Ticket detail and conversation
- [ ] AI triage output
- [ ] Workflow result with retrieved source documents
- [ ] Reject-feedback form
- [ ] Revised recommendation awaiting review
- [ ] Approved reply draft before sending
- [ ] Knowledge base document list
- [ ] AI assistant answer with citations

## Demo safety checklist

- Use only synthetic customer data.
- Never show `.env`, API keys, credentials, or personal inbox contents.
- Ensure email sending is disabled or pointed to a safe test recipient during public demonstrations. If live SMTP is configured, confirm the recipient before every send.
- Do not claim SLA or average-resolution metrics unless the dataset contains reliable timestamp fields and the metrics are actually computed.
- Use a test ticket and test email address for the recording.

## Portfolio project description draft

**SupportPilot AI — Agentic Customer Support Automation with RAG and Human Approval**

Built a customer-support workspace that combines ticket triage, knowledge-grounded responses, and a LangGraph workflow with human approval. The application classifies tickets, retrieves relevant support documentation from a vector database, generates resolution recommendations and editable customer replies, and supports rejection with feedback and revision before approval. Customer email delivery remains a separate explicit action.

**Tech:** React, TypeScript, FastAPI, PostgreSQL, Qdrant, embeddings, LangGraph, Docker Compose, Groq-compatible LLM integration.

**Highlights:** ticket management, AI classification, RAG with source citations, knowledge ingestion, durable workflow checkpointing, human-in-the-loop approval/revision, editable reply drafts, and explicit email sending.
