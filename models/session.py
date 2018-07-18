from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql://localhost/ecommerce", echo=True)

Session=sessionmaker(bind=engine)
session_1=Session()

