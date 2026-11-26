# Human Review: Reject and Revise

- Approval accepts the reviewed recommendation and reply. Email remains a separate explicit send action.
- Rejection requires reviewer feedback.
- LangGraph resumes from the saved checkpoint, uses the feedback to revise the recommendation, regenerates the reply, and pauses at the human review interrupt again.
- The reviewer can approve the revision or reject it again with new feedback.
- A workflow reply cannot be sent from the UI until the workflow has been approved.

## Suggested test
1. Run AI review on a ticket.
2. Enter reviewer feedback such as: "Do not promise a refund. Ask for the transaction ID first."
3. Click **Reject & revise**.
4. Confirm a revised recommendation and draft appear, and the review controls return.
5. Approve, then confirm Send email is enabled. Sending is still a separate action.
