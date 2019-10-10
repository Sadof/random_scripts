import sqlite3


conn = sqlite3.connect("weather.db")
c = conn.cursor()
c.execute('''CREATE TABLE weather
            (year INT, date DATE, T REAL,
            F REAL, wind REAL )''')
            #P INT DEFAULT 0,
            #rain INT DEFAULT 0, snow INT DEFAULT 0
print("Created")
 
