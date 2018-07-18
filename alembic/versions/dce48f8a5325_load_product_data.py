"""load product data

Revision ID: dce48f8a5325
Revises: 07678e3c6d41
Create Date: 2018-07-15 19:07:21.785166

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dce48f8a5325'
down_revision = '5d6535f83406'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('INSERT INTO products (stock_code,description,unit_price) '
                ' (SELECT stock_code,description,unit_price FROM  invoices )'
                ' ON CONFLICT (stock_code, unit_price) DO NOTHING;')


    op.execute('COMMIT')



def downgrade():
    op.execute("TRUNCATE TABLE products;")
    op.execute('COMMIT')
