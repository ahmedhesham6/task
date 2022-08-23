"""create balances view

Revision ID: e6c2e7fe1b0e
Revises: c0e2bc0264b1
Create Date: 2022-08-15 09:38:23.582952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6c2e7fe1b0e'
down_revision = 'c0e2bc0264b1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    conn = op.get_bind()
    conn.execute(sa.text(
        """
            create view balances  as select user_id, deposits , coalesce(withdraws,0) as withdraws , deposits - coalesce(withdraws,0) as balance from balance_events be 
            left join (
                        select user_id as ui, sum(amount) as deposits from balance_events be2 where type = 'deposit' group by user_id
                        ) deposits on deposits.ui = be.user_id 
            left join (
                        select user_id as ui, coalesce(sum(amount),0) as withdraws from balance_events be3 where type = 'withdraw' group by user_id
                        ) withdraws on withdraws.ui = be.user_id 
            group by user_id, deposits, withdraws;
        """
    )
    )


def downgrade() -> None:
    conn = op.get_bind()
    conn.execute(sa.text(
        """
            drop view balances;
        """
    )
    )
