from sqlalchemy import Column,String,DateTime,Integer,Float
from models.base import Base
from models import session

class Invoice(Base):
    __tablename__='invoices'
    id=Column(Integer, primary_key=True)
    invoice_number=Column(String)
    stock_code=Column(String)
    description=Column(String)
    quantity=Column(Integer)
    invoice_date=Column(DateTime)
    customer_id=Column(Integer)
    unit_price=Column(Float)
    country=Column(String)

    def create(self):
        session.session_1.add(self)
        session.session_1.commit()








