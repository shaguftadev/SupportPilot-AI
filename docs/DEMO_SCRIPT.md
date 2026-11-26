# SupportPilot AI — Realistic Demo Walkthrough

## Demo setup
The database seeds 32 realistic tickets across Billing, Account, Technical, and Product. A subset includes customer/agent conversation history so the ticket detail view looks like an active support workspace. Seed data is idempotent: missing demo ticket numbers are added on startup; existing tickets and replies are not overwritten.

## Recommended walkthrough
1. Open the dashboard and show the mix of open, in-progress, priorities, and categories.
2. Open **SP-1004 — Charged twice for monthly subscription** and review the conversation.
3. Run **AI Review & Recommendation**. Explain classification, routing, knowledge retrieval, and recommendation.
4. Reject with feedback such as: “Do not promise a refund. Ask for transaction references and explain that billing will compare the records.”
5. Review the revised recommendation and customer reply, then approve.
6. Edit the customer-facing draft and only then use the separate send action.
7. Demonstrate an urgent technical ticket, such as **SP-1032 — Service unavailable for our entire team**, and explain escalation.

## Knowledge base demo content
Upload the text documents from `demo_documents/knowledge_base/` through the Knowledge Base screen before the demo. They cover billing/refunds, account security, technical troubleshooting, workspace permissions, and escalation guidance. Upload each file once; these documents are designed to provide grounded retrieval for the seeded tickets.

## Safety note
All sample customers, email addresses, ticket IDs, and incidents are fictional. The workflow does not automatically send customer emails or perform refunds. Human approval is required, and sending remains a separate explicit action.
