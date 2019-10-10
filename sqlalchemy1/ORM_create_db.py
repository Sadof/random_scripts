from sqlalchemy import create_engine, MetaData, Column, Table , Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

db_string = 'postgresql+psycopg2://postgres:Sadof123@localhost/new_test'
e = create_engine(db_string, echo = True ) # ,echo = True for log
Base = declarative_base()

class Customers(Base):
	__tablename__ = "customers"
	id = Column(Integer, primary_key = True)
	name = Column(String)
	address = Column(String)
	email = Column(String)


class Invoive(Base):
	__tablename__ = "invoices"
	id = Column(Integer, primary_key = True)
	custid = Column(Integer, ForeignKey("customers.id"))
	invno = Column(Integer)
	amount = Column(Integer)
	amount = Column(Integer)
	customer = relationship("Customers", back_populates = "invoices")

Customers.invoices = relationship("Invoice", order_by = Invoive.id, back_populates="customers")
def create():
	Base.metadata.create_all(e)

def session_commit():
	Session = sessionmaker(bind = e)
	session = Session()

	c1 = Customers(name = "Sadof", address = "Sadovaj", email = "maksuma95@mail.ru")

	session.add(c1)
	session.commit()


def session_all():
	Session = sessionmaker(bind = e)
	session= Session()
	result = session.query(Customers).all()

	for row in result:
		print(row.name, row.address, row.email)


def session_get(id):
	Session = sessionmaker(bind = e)
	session = Session()
	x = session.query(Customers).get(id)
	print(x.name, x.address, x. email)


#update row with given id in column with value Kappa best comment ever
def session_update(id, column, value):
	Session = sessionmaker(bind = e)
	session = Session()
	x = session.query(Customers).get(id)
	setattr(x,column,value)
	session.commit()


#updaet many rows with some filter
def session_bulk_update():
	Session = sessionmaker(bind = e)
	session = Session()
	x = session.query(Customers).filter(Customers.id != 1).update({Customers.name:"Mr. " + Customers.name}, synchronize_session = False)
	session.commit()


#search
def session_like_filter(column, string):
	Session = sessionmaker(bind = e)
	session = Session()
	x = session.query(Customers).filter(getattr(Customers,column).like(string))
	if x.count():
		for row in x:
			print(row.name, row.address, row.email)
	else:
		print("No result")


def session_in_filter(column, arr):
	Session = sessionmaker(bind = e)
	session = Session()
	x = session.query(Customers).filter(getattr(Customers,column).in_(arr))
	for row in x:
		print(row.id, row.name, row.address, row.email)

def session_add_filter():
	from sqlalchemy import and_
	Session = sessionmaker(bind = e)
	session = Session()
	x = session.query(Customers).filter(Customers.id >= 3, Customers.name.like("%ad%"))
	y = session.query(Customers).filter(and_(Customers.id >= 3, Customers.name.like("%ad%")))
	print("X")
	for row in x:
		print(row.id, row.name, row.address, row.email)
	print("Y")
	for row in y:
		print(row.id, row.name, row.address, row.email)

def session_or_filter():
	from sqlalchemy import or_
	Session = sessionmaker(bind = e)
	session = Session()
	x = session.query(Customers).filter(or_(Customers.id >= 3, Customers.name.like("%re%")))
	for row in x:
		print(row.id, row.name, row.address, row.email)

def session_text(string):
	from sqlalchemy import text
	Session = sessionmaker(bind = e)
	session = Session()
	x = session.query(Customers).filter(text(string))
	for row in x:
		print(row.id, row.name)
	y = session.query(Customers).filter(text("id = :value")).params(value = 1).one()

	print(y.id, y.name)

session_all()