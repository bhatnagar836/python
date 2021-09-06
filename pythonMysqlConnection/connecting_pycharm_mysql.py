import mysql.connector

meradatabase= mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    port='3306',
    database='abc_company'
)

meracursor= meradatabase.cursor()

meracursor.execute('SELECT * FROM employee')

emp= meracursor.fetchall()

for employees in emp:
    print (employees )

    print("\n\n")
    
meracursor.execute('SELECT * FROM department')
dept=meracursor.fetchall()

for departments in dept:
    print(departments)

