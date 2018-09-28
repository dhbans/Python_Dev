import sqlite3
from util.logger import get_logger

logger = get_logger()

conn = sqlite3.connect('Training_DHruv11.db')
c = conn.cursor()


# This exercise one from W3 site, finding where city is Berlin
c.execute('select City from Emp_data where City ="Berlin"')

result = c.fetchall()
logger.info('Lenght of list is %s',len(result))
for row in result:
    logger.info(row)

# Finding where city is not equal to Berlin

c.execute('select City from Emp_data where City <>"Berlin"')
result = c.fetchall()
logger.info('Lenght of list is %s',len(result))
for row in result:
    logger.info(row)

# Select where customerID is having value equal to 32

c.execute('select * from Emp_data where CustomerID="32"')
result = c.fetchall()
logger.info('Lenght of list is %s',len(result))
for row in result:
    logger.info(row)

# Select all records where the City column has the value 'Berlin' and the PostalCode column has the value 12209

c.execute('select * from Emp_data where City="Berlin" and PostalCOde ="12209" ')
result = c.fetchall()
logger.info('Lenght of list is %s',len(result))
for row in result:
    logger.info(row)

# Select all records where the City column has the value 'Berlin', and also the records where the City column has the value 'London'

c.execute('select * from Emp_data where City="Berlin" or City = "London" ')
result = c.fetchall()
logger.info('Lenght of list is %s',len(result))
for row in result:
    logger.info(row)