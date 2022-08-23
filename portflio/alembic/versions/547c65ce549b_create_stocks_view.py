"""create stocks view

Revision ID: 547c65ce549b
Revises: 46e9a183fd26
Create Date: 2022-08-16 16:20:00.427886

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '547c65ce549b'
down_revision = '46e9a183fd26'
branch_labels = None
depends_on = None


def upgrade() -> None:
    conn = op.get_bind()
    conn.execute(sa.text(
        """
            create view stocks as select stock_id, se."name" , se.price as price , se.availability , 
                coalesce(max_dp,price) as max_day,
                coalesce(min_dp,price) as min_day,
                coalesce(max_hp,price) as max_hour,
                coalesce(min_hp,price) as min_hour
                from (	
                    select distinct on (stock_id) stock_id ,"name", price, availability
                    from stock_events se 
                    order by stock_id, "timestamp" desc
                    ) se
                left join (
                    select stock_id as si, max(price) as max_dp, min(price) as min_dp from stock_events se2 
                    where se2."timestamp" > 'today'::TIMESTAMP and se2."timestamp" < 'tomorrow'::TIMESTAMP
                    group by se2.stock_id
                    ) daily on daily.si = se.stock_id 
                left join (
                    select stock_id as si, max(price) as max_hp, min(price) as min_hp from stock_events se3 
                    where se3."timestamp" > now()- interval '1 hour'
                    and se3."timestamp" <= now()
                    group by se3.stock_id
                ) hourly on hourly.si = se.stock_id 
        """
    )
    )


def downgrade() -> None:
    conn = op.get_bind()
    conn.execute(sa.text(
        """
            drop view stocks;
        """
    )
    )
