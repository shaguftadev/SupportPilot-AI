"""Add persisted ticket replies

Revision ID: 0002_ticket_replies
Revises: 0001_initial
"""
from alembic import op
import sqlalchemy as sa

revision = "0002_ticket_replies"
down_revision = "0001_initial"
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        "ticket_replies",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("ticket_id", sa.String(length=36), sa.ForeignKey("tickets.id", ondelete="CASCADE"), nullable=False),
        sa.Column("sender_type", sa.String(length=20), nullable=False, server_default="agent"),
        sa.Column("sender_name", sa.String(length=120), nullable=False, server_default="Jordan Davis"),
        sa.Column("body", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
    )
    op.create_index("ix_ticket_replies_ticket_id", "ticket_replies", ["ticket_id"])

def downgrade():
    op.drop_index("ix_ticket_replies_ticket_id", table_name="ticket_replies")
    op.drop_table("ticket_replies")
