"""create customer table

Revision ID: f4fdaeb21f07
Revises: dce48f8a5325
Create Date: 2018-07-15 19:48:24.937923

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4fdaeb21f07'
down_revision = 'dce48f8a5325'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'customers',
        sa.Column('id',sa.Integer,primary_key=True,autoincrement=True),
        sa.Column('customer_id', sa.Integer,nullable=True),
        sa.Column('password', sa.String(45), nullable=True),
        sa.Column('country', sa.String(45), nullable=True)
    )

    op.execute('COMMIT')
    op.create_index(index_name='index_on_ci_c', table_name='customers', columns=['customer_id', 'country'],
                    unique=True)
    op.execute('COMMIT')


def downgrade():
    op.drop_table('customers')
    op.execute('COMMIT')
