"""load data

Revision ID: d9664a60b59d
Revises: f26cb9474180
Create Date: 2018-07-14 21:53:18.551643

"""
import os
from alembic import op
import sys
sys.path.append(os.path.join(os.getcwd(), '../../'))

import csv




# revision identifiers, used by Alembic.
revision = 'd9664a60b59d'
down_revision = 'f26cb9474180'
branch_labels = None
depends_on = None


def upgrade():
    file_name = 'data/data.csv'
    path = os.getcwd()
    file_path = os.path.join(path, file_name)
    # with open(file_path, newline='',encoding='latin-1') as csvfile:
    #     reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    #     next(reader, None)
    #     for row in reader:
    #         new_invoice = invoice.Invoice(invoice_number=row[0], stock_code=row[1], description=row[2], quantity=row[3],
    #                               invoice_date=row[4], unit_price=row[5], customer_id=row[6], country=row[7])
    #         new_invoice.create()

    op.execute("COPY invoices (invoice_number,stock_code,description,quantity,invoice_date,unit_price,customer_id,country) FROM '"+file_path+"' ENCODING 'latin-1' DELIMITER ',' QUOTE '\"' CSV HEADER;")



def downgrade():
    op.execute("TRUNCATE TABLE invoices;")




