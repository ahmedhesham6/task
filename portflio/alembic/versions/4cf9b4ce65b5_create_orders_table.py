"""create orders table

Revision ID: 4cf9b4ce65b5
Revises: 547c65ce549b
Create Date: 2022-08-18 12:12:56.796419

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = '4cf9b4ce65b5'
down_revision = '547c65ce549b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "orders",
        sa.Column(
            "id", UUID, server_default=sa.text("gen_random_uuid()"), primary_key=True
        ),
        sa.Column(
            "stock_id", UUID, nullable=False
        ),
        sa.Column(
            "user_id", UUID, nullable=False
        ),
        sa.Column("type", sa.String(50), nullable=False),
        sa.Column("amount", sa.Integer, nullable=False),
        sa.Column("unit_price", sa.Numeric(
            precision=10, scale=2), nullable=False),
        sa.Column("total", sa.Numeric(
            precision=10, scale=2), nullable=False),
        sa.Column(
            "timestamp", sa.DateTime(), nullable=False
        ),
    )


def downgrade() -> None:
    op.drop_table("balance_events")
