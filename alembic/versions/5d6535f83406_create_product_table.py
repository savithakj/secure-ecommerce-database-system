"""create product table


Revision ID: 5d6535f83406
Revises: d9664a60b59d
Create Date: 2018-07-15 17:48:08.604657

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d6535f83406'
down_revision = 'd9664a60b59d'
branch_labels = None
depends_on = None


def upgrade():

    op.create_table(
        'products',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('stock_code', sa.String(45),nullable=True),
        sa.Column('description', sa.String(45), nullable=True),
        sa.Column('unit_price', sa.Float, nullable=True)

    )

    op.execute('COMMIT')
    op.create_index(index_name='index_on_d', table_name='products', columns=['description'], unique=True)
    op.execute('COMMIT')


def downgrade():
    op.drop_table('products')
    op.execute('COMMIT')
