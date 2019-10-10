import random
import sqlite3

name_list = ['Suzanne Rupp', 'Heike Leday', 'Wendi Mcguire','Contessa Sama',
 'Franklin Depp', 'Zona Anzaldua', 'Madlyn Minjares', 'Jadwiga Schreiner',
'Nichole Cavin', 'Jerome Abbate', 'Gertrude Barcenas','Merlyn Springfield',
'Lucia Cota','Lavonda Yocom','Patrica Rines','Marc Pennypacker',
 'Breanna Keesler','Rey Boring','Belle Louque','Delila Wickstrom',
'Beatris Garbarino', 'Esteban Charest','Kathline Davenport','Reid Siddiqi',
'Virgie Magnus','Hai Oaks','Osvaldo Eakes','Jaleesa Kettering',
'Gus Jeffery','Andres Cormack']
work_list = [['worker',100],['programmist',200],['economist',200],
             ['artist',180], ['actor',300], ['police',150],
             ['driver',120],['student',10]]

conn = sqlite3.connect('people.db')
c = conn.cursor()
cache = tuple()
a = list()
c.execute("SELECT * FROM stocks" )
ID = len(c.fetchall())
name_list_len = len(name_list)
work_list_len = len(work_list)

for i in range(int(input())):
    bd = random.randint(1970,2000)
    work =random.randint(0,work_list_len - 1)
    a.append([ID, name_list[random.randint(0,name_list_len - 1)], bd , 2019 - bd , work_list[work][0],work_list[work][1]])
    ID += 1
cache = tuple(a)
print(cache)
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?,?)',cache)

conn.commit()

conn.close()

     
