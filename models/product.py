from sqlalchemy import Column,String,DateTime,Integer,Float
from models.base import Base
from models import session

class Product:
    __tablename__='products'
    id = Column(Integer, primary_key=True)
    stock_code = Column(String)
    description = Column(String)
    unit_price = Column(Float)

