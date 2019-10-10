import requests
import sqlite3


conn = sqlite3.connect("weather.db")
c = conn.cursor()
c.execute("SELECT * FROM weather")
for i in c.fetchall():
	print(i)
conn.commit()

conn.close()
a = input()
