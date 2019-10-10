from sqlalchemy import create_engine, MetaData, Column, Table , Integer, String, ForeignKeyConstraint
from sqlalchemy.ext.declarative import declarative_base



db_string = 'postgresql+psycopg2://postgres:Sadof123@localhost/new_test'
e = create_engine(db_string ,echo = True)
Base = declarative_base()

class Customers(Base):
	__tablename__ = "customers"
	id = Column(Integer, primary_key = True)
	name = Column(String)
	adress = Column(String)
	email = Column(String)


Base.metadata.create_all(e)