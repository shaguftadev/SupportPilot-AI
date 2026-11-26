# Public Portfolio Demo Deployment (Recommended)

## Architecture
- **Frontend:** Vercel (static React/Vite)
- **API:** Railway (Dockerized FastAPI)
- **Database:** Railway managed PostgreSQL
- **Vector DB:** Qdrant Cloud
- **LLM:** Groq API

This is a portfolio demo, not a production multi-tenant system. Use synthetic data only.

## Before deploying
1. Create a GitHub repository and push the project branch. Keep `.env` out of Git.
2. Create a Railway project and add PostgreSQL.
3. Deploy the API service from the same repository with its root directory set to the repo root and Dockerfile path `backend/Dockerfile`.
4. Set the API service variables listed below. Railway should supply `PORT`; the Dockerfile supports it.
5. Create a Qdrant Cloud cluster. Copy its HTTPS endpoint and API key.
6. Deploy the frontend to Vercel. Set Root Directory to `frontend` and `VITE_API_BASE_URL` to the public API URL plus `/api`, e.g. `https://your-api-domain.up.railway.app/api`.
7. After the Vercel URL is known, add it to `CORS_ORIGINS` on the API service. Include the API URL only if required by local/admin tools. Redeploy API.
8. Upload demo knowledge-base documents through the deployed UI.

## Railway API environment variables
- `APP_ENV=production`
- `APP_SECRET` = generate a long random secret
- `DEMO_MODE=true` (IMPORTANT: email delivery is simulated; it will not send real email)
- `DATABASE_URL` = Railway PostgreSQL connection URL. Use the internal/private URL when available.
- `QDRANT_URL` = Qdrant Cloud HTTPS endpoint
- `QDRANT_API_KEY` = Qdrant Cloud API key
- `QDRANT_COLLECTION=supportpilot_knowledge`
- `LLM_PROVIDER=groq`
- `GROQ_API_KEY` = your Groq key (secret)
- `GROQ_MODEL=openai/gpt-oss-120b`
- `CORS_ORIGINS=https://YOUR-VERCEL-DOMAIN.vercel.app`
- `UPLOAD_DIR=/app/uploads`
- `MAX_UPLOAD_MB=20`
- `WORKFLOW_CHECKPOINT_ENABLED=true`
- Leave SMTP variables unset for the public demo.

**Persistence:** add a Railway volume mounted at `/app/uploads` if you want uploaded source files retained between deployments. The relational DB and Qdrant store metadata and vectors separately.

## Frontend Vercel environment
- `VITE_API_BASE_URL=https://YOUR-RAILWAY-API-DOMAIN/api`

## Demo safety
- This deployment uses `DEMO_MODE=true`; the Send Email action is simulated and logged in the app.
- All ticket/customer data is fictional.
- Never commit `.env`, keys, passwords, SMTP credentials, or real customer data.
- Do not expose PostgreSQL or Qdrant to public access beyond provider's secure endpoint/API-key controls.
- Use a separate demo Groq key with limits if possible.

## Smoke test
1. Open the public frontend.
2. Confirm dashboard loads tickets.
3. Open a ticket and run analysis.
4. Run the LangGraph workflow and confirm it pauses for approval.
5. Reject with feedback and confirm revised recommendation.
6. Approve and send a reply; verify delivery says `simulated` (no real email).
7. Upload a demo PDF/TXT and ask a KB-grounded question.
8. Ask an unknown question and verify the app abstains rather than fabricates.

## Troubleshooting
- API `/ready` should return ready.
- API logs should show checkpointer initialized.
- If frontend API calls fail, verify `VITE_API_BASE_URL` includes `/api`, Vercel redeployed after setting it, and API `CORS_ORIGINS` exactly matches the frontend origin.
- Qdrant authentication errors: verify endpoint and API key; endpoint must be HTTPS.
- PostgreSQL URL may be `postgres://` or `postgresql://`; backend normalizes both.
