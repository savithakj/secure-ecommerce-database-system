"""load customer data

Revision ID: 7b0da3755a1c
Revises: f4fdaeb21f07
Create Date: 2018-07-15 19:52:15.582798

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b0da3755a1c'
down_revision = 'f4fdaeb21f07'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('INSERT INTO customers (customer_id,country) '
                ' (SELECT customer_id,country FROM  invoices '
                'WHERE invoices.customer_id IS NOT NULL )'
                ' ON CONFLICT (customer_id, country) DO NOTHING ;')


    op.execute('COMMIT')


def downgrade():
    op.execute("TRUNCATE TABLE customers;")
    op.execute('COMMIT')
