# SupportPilot AI

Portfolio-ready AI customer support workspace featuring ticket management, document ingestion, local semantic embeddings, Qdrant retrieval, cited RAG answers, AI ticket analysis, response drafting, and human review.

> This is a portfolio/demo application, not a security-audited production service. Before real customer deployment, add authentication/authorization, secret management, backups, monitoring, rate limiting, privacy controls, and a formal security review.

## Quick start (Docker)

1. Install Docker Desktop and ensure it is running.
2. Copy `.env.example` to `.env`.
3. Optionally add your Groq API key to `GROQ_API_KEY`. The app includes a grounded demo fallback when no LLM key is configured.
4. From this directory run:

   ```powershell
   docker compose up --build
   ```

5. Open **http://localhost:8080** (UI), **http://localhost:8000/docs** (API docs), and **http://localhost:6333/dashboard** (Qdrant dashboard).

The first knowledge-base upload downloads the FastEmbed model in the API container. This can take a few minutes and requires internet access.

## Demo walkthrough

- Explore seeded tickets on the dashboard.
- Open a ticket and try **Run agentic workflow**. LangGraph performs triage, conditional routing, Qdrant retrieval, resolution recommendation, and reply drafting; the draft remains subject to human review.
- You can still use **AI Analyze** and **Draft customer reply** independently.
- Go to Knowledge Base and upload `demo_documents/SupportPilot_Demo_FAQ.txt` (or your own PDF, DOCX, or TXT support document).
- Ask the AI Assistant a question about the uploaded document.
- Review source citations and use the generated answer as a draft; agents remain in control.

## Stack

- Frontend: React, TypeScript, Vite, CSS
- API: FastAPI, Pydantic, SQLAlchemy
- Database: PostgreSQL
- Vector search: Qdrant
- Embeddings: FastEmbed `BAAI/bge-small-en-v1.5` (local)
- LLM: Groq API (configurable); deterministic grounded demo fallback without key
- Deployment: Docker Compose

## API endpoints

- `GET /health` process health
- `GET /ready` dependency readiness
- `GET /api/dashboard/stats` dashboard summary
- `GET /api/tickets` list/search/filter
- `POST /api/tickets` create
- `GET /api/tickets/{id}` details
- `PATCH /api/tickets/{id}` update
- `POST /api/tickets/{id}/analyze` AI ticket analysis
- `POST /api/tickets/{id}/draft` response draft
- `POST /api/tickets/{id}/workflow` LangGraph agentic workflow
- `GET /api/documents` knowledge sources
- `POST /api/documents/upload` ingest PDF/DOCX/TXT
- `DELETE /api/documents/{id}` remove source
- `POST /api/assistant/chat` RAG chat

## Local backend development (optional)

Requires Python 3.11+. From `backend/`: create a venv, install `requirements.txt`, then run `uvicorn app.main:app --reload`. You still need PostgreSQL and Qdrant. Docker is the recommended path because it avoids Windows environment drift.

## Architecture

See `docs/ARCHITECTURE.md` and `docs/AGENTIC_WORKFLOW.md`.

## Interview/demo materials

See `docs/DEMO_SCRIPT.md` and `docs/INTERVIEW_NOTES.md`.


### Groq model update (November 2026)

The default Groq model is `openai/gpt-oss-120b`. The previously used `llama-3.3-70b-versatile` model was retired for free/developer tiers. If you already created a `.env` file, make sure it contains:

```env
GROQ_MODEL=openai/gpt-oss-120b
```

Provider request errors are logged and the app falls back to demo-mode ticket analysis, reply drafting, and knowledge answers instead of returning a 500 error.


## Sending real customer emails

The **Send email** action delivers the edited reply to the ticket's customer email address through SMTP, then stores it in conversation history after the SMTP server accepts the message. Configure the SMTP variables in your root `.env` file first. For Gmail, use `smtp.gmail.com`, port `587`, TLS enabled, your Gmail address as `SMTP_USERNAME` and `SMTP_FROM_EMAIL`, and a Google App Password as `SMTP_PASSWORD` (not your regular password). Use a test ticket addressed to your own email before sending to any real customer. Restart Docker Compose after changing `.env`. If SMTP is not configured, the API returns a clear configuration error and does not mark the reply as sent or save it as a sent message.


## Milestone 3 — Durable Workflow & Human Approval

The LangGraph support workflow now uses PostgreSQL checkpoint persistence (`langgraph-checkpoint-postgres`). Each run receives a workflow/thread ID and pauses at a human-review interrupt after generating its recommendation and draft. The UI can approve or reject the draft; approval resumes the graph and records `approved_for_send`. Sending email remains a separate explicit action. Checkpoint state can be retrieved by workflow ID, and the frontend remembers the latest workflow ID per ticket in browser local storage so it can restore a saved checkpoint when the ticket is reopened.

### Approval flow
1. Run AI review.
2. Workflow triages, routes, retrieves knowledge, recommends a resolution, and drafts a reply.
3. LangGraph pauses at human-review interrupt and checkpoints state in PostgreSQL.
4. Agent edits the draft and selects Approve draft or Reject recommendation.
5. Approval resumes the workflow and marks the draft approved for sending.
6. Agent sends the email separately; the workflow does not send emails automatically.

Checkpointing can be disabled with `WORKFLOW_CHECKPOINT_ENABLED=false` (the current workflow approval UI requires a checkpointer).

## Realistic demo dataset

The backend seeds 32 fictional support tickets across Billing, Account, Technical, and Product categories. Several tickets have conversation history for demo purposes. The seed process is idempotent and adds missing sample ticket numbers without overwriting existing records.

Before a portfolio demo, upload the five files under `demo_documents/knowledge_base/` using the Knowledge Base UI to populate retrieval with realistic support policies and troubleshooting guidance.


## Expanded demo dataset

The seed script includes 100 fictional support tickets (SP-1001 through SP-1100), varied categories, priorities, statuses, and selected conversation histories. It inserts missing demo records without overwriting existing tickets. The Knowledge Base folder includes additional SLA, billing, integrations/API, privacy, and workspace administration guides.


## Expanded demo dataset

This version seeds **600 fictional support tickets** across billing, account, technical, product, and general categories. It includes varied priorities and statuses, selected conversation histories, and a CSV export at `demo_documents/expanded_demo_tickets.csv`. The seed is idempotent and inserts missing records only.
