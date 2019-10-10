from sqlalchemy import create_engine, MetaData, Column, Table , Integer, String, ForeignKeyConstraint




db_string = 'postgresql+psycopg2://postgres:Sadof123@localhost/new_test'

e = create_engine(db_string ,echo = True)


def flight_execute():
	flights = e.execute(
		""" select f.flight_id,a.airport_name,f.actual_departure,f.actual_arrival from flights as f join airports as a on f.arrival_airport = a.airport_code 
			where a.city='St. Petersburg' and f.actual_arrival is not null""")

	for flight in flights.fetchall():
		print(*flight)


metadata = MetaData()
user_table = Table('user',metadata,
				Column('id', Integer, primary_key = True),
				Column('username', String),
				Column('password', String)
				)
post_table = Table('post',metadata,
				Column('id', Integer, primary_key = True),
				Column("text", String, nullable = False),
				Column("id_author", Integer),
				ForeignKeyConstraint(
					["id_author"],
					["user.id"])
				)
metadata.create_all(e)


print(user_table.c.username == "ed")
print(str(user_table.c.username == "ed"))


