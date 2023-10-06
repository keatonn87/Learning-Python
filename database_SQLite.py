import sqlite3
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("""CREATE TABLE Ages(
             name VARCHAR(128),
             age INTEGER
             )"""
         )
def add_people(sName, iAge):
    with conn:
        c.execute("INSERT INTO Ages VALUES (:name, :age)", {'name':sName, 'age':iAge})

lPeople = [('Claire', 16), ('Dara', 25), ('Annaliesse', 34), ('Ailiegh', 26), ('Kellan', 24)]
for tItem in lPeople:
    sName, iAge = tItem
    add_people(sName, iAge)

c.execute("SELECT hex(name || age) AS X FROM Ages ORDER BY X")
print(c.fetchall())

conn.commit()
conn.close()