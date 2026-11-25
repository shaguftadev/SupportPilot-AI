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
- Open a ticket, run **AI Analyze**, and generate a suggested reply.
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
- `GET /api/documents` knowledge sources
- `POST /api/documents/upload` ingest PDF/DOCX/TXT
- `DELETE /api/documents/{id}` remove source
- `POST /api/assistant/chat` RAG chat

## Local backend development (optional)

Requires Python 3.11+. From `backend/`: create a venv, install `requirements.txt`, then run `uvicorn app.main:app --reload`. You still need PostgreSQL and Qdrant. Docker is the recommended path because it avoids Windows environment drift.

## Architecture

See `docs/ARCHITECTURE.md`.

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
