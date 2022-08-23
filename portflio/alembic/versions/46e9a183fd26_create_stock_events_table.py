"""create stock_events table

Revision ID: 46e9a183fd26
Revises: e6c2e7fe1b0e
Create Date: 2022-08-16 13:38:37.107425

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = '46e9a183fd26'
down_revision = 'e6c2e7fe1b0e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "stock_events",
        sa.Column(
            "id", UUID, server_default=sa.text("gen_random_uuid()"), primary_key=True
        ),
        sa.Column(
            "stock_id", UUID, nullable=False
        ),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("price", sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column("availability", sa.Integer, nullable=False),
        sa.Column(
            "timestamp", sa.DateTime(), nullable=False
        ),
    )


def downgrade() -> None:
    op.drop_table("balance_events")
