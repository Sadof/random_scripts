from sqlalchemy import create_engine
import os

if os.path.exists("some.db"):
    os.remove("some.db")
e = create_engine("sqlite:///some.db")
e.execute("""
	create table users(
		user_id integer primary key,
		username varchar,
		password varhar
		)
	""")



e.execute(""" insert into users(username, password) values ('Quest','qwerty123')""")
e.execute(""" insert into users(username, password) values ('Sadof','qwerty123')""")
e.execute(""" insert into users(username, password) values ('Mesuni','qwerty123')""")


users = e.execute(""" select username, password from users where password='qwerty123' """)
for user in users.fetchall():
	print(*user)


users.close()