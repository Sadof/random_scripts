import sqlite3
conn = sqlite3.connect('people.db')
c = conn.cursor()
c.execute('''CREATE TABLE stocks
            (ID INTEGER PRIMARY KEY,
            name text, bd text,
            age int, work text,
            salary real)''')
print("CREATED")

conn.commit()

conn.close()
