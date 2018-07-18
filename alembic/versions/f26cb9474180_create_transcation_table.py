"""create transcation_table

Revision ID: f26cb9474180
Revises: 
Create Date: 2018-07-14 21:06:51.255119

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'f26cb9474180'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'invoices',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('invoice_number', sa.String(45), nullable=True),
        sa.Column('stock_code', sa.String(45), nullable=True),
        sa.Column('description', sa.String(45), nullable=True),
        sa.Column('quantity', sa.Integer, nullable=True),
        sa.Column('invoice_date', sa.DateTime, nullable=True),
        sa.Column('unit_price', sa.Float, nullable=True),
        sa.Column('customer_id', sa.Integer, nullable=True),
        sa.Column('country', sa.String(45), nullable=True)
    )
    op.execute('COMMIT')



def downgrade():
    # op.drop_table('alembic_version')
    op.drop_table('invoices')

