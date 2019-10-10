import sqlite3

numbers = (0,1,2,3,4,5,6,7,8,9)

def read_db():
    conn = sqlite3.connect("people.db")
    c = conn.cursor()
    c.execute("SELECT * FROM stocks" )
    data = c.fetchall()
    conn.commit()
    conn.close()
    return data

def delete_data(ID):
    conn = sqlite3.connect('people.db')
    c = conn.cursor()
    data = (ID,)
    c.execute("DELETE FROM stocks WHERE ID = ?",data)
    print("DELETED")
    conn.commit()
    conn.close() 
    
def insert_data(name,bd,work,salary):
    result = "INSERTED"
    conn = sqlite3.connect("people.db")
    c = conn.cursor()
    c.execute("SELECT ID FROM stocks ORDER BY ID DESC" )
    ID = c.fetchone()
    print(name, bd, work, salary)
    if name == '' or bd == '' or work == '' or salary == '':
        result = "EMPTY"
        print("EMPTY")
        return result
    print(2)
    for i in name:
        if i in str(numbers):
            result = "NOPE"
    for i in work:
        if i in str(numbers):
            result = "NOPE"
    if result == "INSERTED":
        data = (ID[0]+1, name, bd, 2019 - int(bd), work, float(salary))
        c.execute('INSERT INTO stocks VALUES (?,?,?,?,?,?)', data)
    conn.commit()
    conn.close()
    return result
    

