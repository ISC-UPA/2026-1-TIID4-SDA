# https://github.com/jpwhite3/northwind-SQLite3
import os
import sys
import sqlite3
con = sqlite3.connect(os.path.join(os.path.dirname(__file__), '..', 'data', 'northwind.db'))
con = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'python.db'))
con = sqlite3.connect('python.db')
cur = con.cursor()


for row in cur.execute("select * from pyversions"):
    print(row)

result =cur.execute('select count(*) from pyversions')
rows = result.fetchone()
print(rows[0])
con.close()

sql= '''
CREATE TABLE pyversions (
branch TEXT PRIMARY KEY,
released_at_year INTEGER,
released_at_month INTEGER,
release_manager TEXT
)
'''
# cur.execute(sql)

# sql = 'INSERT INTO pyversions VALUES ("2.6", 2008, 10, "Barry Warsaw")'
# cur.execute(sql)
# con.commit()

# c:\>sqlite3 python.db "select * from pyversions"
'''
branch = 3.9
released_at_year = 2020
released_at_month = 10
release_manager = 'Łukasz Langa'
sql = f'INSERT INTO pyversions VALUES ({branch}, {released_at_year}, {released_at_month}, "{release_manager}")'
print(sql)
cur.execute(sql)
con.commit()
'''

'''
branch = 1.3
released_at_year = 2026
released_at_month = 2
release_manager = 'Charlie Langa'
sql = 'INSERT INTO pyversions VALUES (?, ?, ?, ?)'
cur.execute(sql, (branch, released_at_year, released_at_month, release_manager))
con.commit()
'''                                     

'''
sql = 'INSERT INTO pyversions VALUES (:branch, :year, :month, :manager)'
cur.execute(sql, dict(year=2020, month=10, branch=1.5, manager='Łukasz Herrera'))
con.commit()
'''

sql = 'select sum(quantity*unitprice*(1-discount)) from "Order Details"'  # pyversions
for row in cur.execute(sql):
    print(row)
'''
result =cur.execute(sql)
row = result.fetchall()
print("----->")
print(row)

result =cur.execute('select count(*) from pyversions')
rows = result.fetchone()
print(rows[0])
con.close()
'''
