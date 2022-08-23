"""create balance events table

Revision ID: c0e2bc0264b1
Revises: 
Create Date: 2022-08-15 08:02:23.835029

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = "c0e2bc0264b1"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "balance_events",
        sa.Column(
            "id", UUID, server_default=sa.text("gen_random_uuid()"), primary_key=True
        ),
        sa.Column("user_id", UUID, nullable=False),
        sa.Column("type", sa.String(50), nullable=False),
        sa.Column("amount", sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column(
            "timestamp", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
    )


def downgrade() -> None:
    op.drop_table("balance_events")
