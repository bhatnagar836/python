import mysql.connector

mydatabase= mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    port='3306',
    database='abc_company'
)

mycursor= mydatabase.cursor()
# Adding row to a existing  table
mycursor.execute("INSERT INTO department (DeptID, DeptName,Location) VALUES (%s,%s,%s)", (6,"Purchase","Pune"))
mydatabase.commit()

