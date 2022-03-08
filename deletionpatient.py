import sqlite3
connection=sqlite3.connect('hospital.db')

getId=input("Enter Id to be deleted")
result=connection.execute("DELETE FROM PATIENTDATAS WHERE ID="+getId)
print("deleted successfully")