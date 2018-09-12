import sqlite3

# opening a db
conn = sqlite3.connect('Training_DHruv11.db')
c = conn.cursor()

c.execute('DROP TABLE EmpData')
# emp_id_list = [1, 2, 3, 4, 5, 6]
# emp_id_name = ['a', 'b', 'c', 'd', 'e']
# emp_id_dep = ['IT', 'HR', 'FIN', 'FMG', 'Sec']
# emp_id_contact = [1, 22, 3, 4, 5, 6]

data_list = [[1,'a','IT',9632255993],[2,'b','HR',9632255339],[3,'c','FIN',0]]
# creating a table in DB
c.execute('CREATE TABLE IF NOT EXISTS  EmpData(Em_id INT, Name varchar(255), Department TEXT , PhoneNo INT)')

for emp in data_list:
                c.execute("INSERT INTO EmpData(Em_id, Name, Department, PhoneNo)values(?,?,?,?)", emp)


conn.commit()
c.close()
conn.close()


