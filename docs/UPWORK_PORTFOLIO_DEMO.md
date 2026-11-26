# SupportPilot AI — Upwork Portfolio Demo Guide

## Recommended 3–4 minute walkthrough

1. **Overview (20–30 seconds):** Show the 600-ticket workspace, queue KPIs, ticket mix, priority distribution, and resolution snapshot.
2. **Ticket analysis (30–40 seconds):** Open a high-priority billing or technical ticket and run AI analysis. Explain classification, priority, sentiment, and summary.
3. **Agentic workflow (60–75 seconds):** Run the workflow and show triage, routing, knowledge retrieval, sources, and the internal recommendation.
4. **Human-in-the-loop (45–60 seconds):** Reject with feedback, show the revised recommendation, then approve. Emphasize that no email is sent automatically.
5. **Customer reply (30–40 seconds):** Edit the draft, and show the explicit send step. Use a demo-safe email configuration when recording.
6. **Knowledge assistant (20–30 seconds):** Ask a policy question and point out source citations. Demonstrate abstention for a question not covered by the uploaded documents, if available.

## Suggested voiceover

“SupportPilot AI is an AI-powered customer-support workspace I built with React, FastAPI, PostgreSQL, Qdrant, and LangGraph. It combines ticket management, AI triage, knowledge-grounded retrieval, agentic workflows, and human approval.

The workspace contains a large synthetic dataset to demonstrate ticket operations. I’ll open a billing issue and run AI analysis. The system identifies the intent, priority, and sentiment, then the agentic workflow routes the ticket and retrieves relevant knowledge-base passages.

The recommendation is internal guidance. A support agent can review it, reject it with feedback, and ask the workflow to revise. The revised response pauses for review again. Once approved, the customer-facing draft can be edited and sent through a separate explicit action. This prevents the AI from autonomously sending customer communications.

The knowledge assistant also answers questions from uploaded documentation and presents retrieved source passages, helping reviewers verify the answer.”

## Portfolio safety checklist

- Use synthetic customer data only.
- Do not expose `.env`, API keys, passwords, or real customer records in the recording.
- Configure a demo-safe email address or avoid actually sending during the video; the app currently warns before sending real email.
- Clearly describe analytics as a demo snapshot. Time-based SLA and average resolution-time analytics are not currently available from the dataset.
- Show the actual running product and avoid claiming features that are not implemented.
