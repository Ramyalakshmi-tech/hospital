import sqlite3
connection=sqlite3.connect('hospital.db')

getNumber=input("Enter number to be deleted")
result=connection.execute("DELETE FROM DOCTORDATAS WHERE NUMBER="+getNumber)
print("deleted successfully")