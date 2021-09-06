import mysql.connector

mydatabase= mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    port='3306',
    database='abc_company'
)

mycursor= mydatabase.cursor()
# Updating a row to a existing  table
mycursor.execute("UPDATE department SET DeptID='7' WHERE DeptID ='6'")
mydatabase.commit()