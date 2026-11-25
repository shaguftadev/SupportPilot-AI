# Interview talking points

## Problem
Support agents spend time searching internal policies, classifying tickets, and writing repetitive responses. SupportPilot centralizes ticket context and retrieves relevant knowledge to assist agents.

## AI/RAG pipeline
1. Extract text from PDF, DOCX, TXT.
2. Split into bounded chunks with source/page metadata.
3. Embed using a local FastEmbed model.
4. Store vectors and payload in Qdrant.
5. Embed user query and retrieve top-k chunks.
6. Prompt the LLM with retrieved context and request a grounded response.
7. Return answer plus citations; human reviews before using.

## Engineering tradeoffs
- Local embeddings reduce external embedding cost and keep document text out of embedding API requests.
- Qdrant separates semantic retrieval from relational ticket data.
- PostgreSQL is used for structured and transactional entities.
- Docker Compose makes the demo reproducible.
- Demo fallback is explicitly not a model inference path; it is a deterministic response based on retrieved context.

## Limitations and next steps
- No auth/tenant isolation yet.
- Ingestion is synchronous and suitable only for small demos.
- Similarity search needs a curated evaluation set and tuning.
- LLM output needs validation and adversarial testing.
- Add workflow orchestration, queue, telemetry, and deployment security before production.
