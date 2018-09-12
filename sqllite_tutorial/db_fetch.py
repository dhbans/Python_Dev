import sqlite3

conn = sqlite3.connect('Training_DHruv11.db')

c = conn.cursor()
c.execute("SELECT * FROM EmpData")

# this while give one entry base on cursor
print(c.fetchone())

# this will give user define size row entries from current cursor position
print(c.fetchmany(2))

# this will give all entries base on cursor
print(c.fetchall())
