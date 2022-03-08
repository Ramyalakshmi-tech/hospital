import sqlite3
connection=sqlite3.connect('hospital.db')
result=connection.execute("SELECT * FROM PATIENTDATAS")
for i in result:
    print("ID",i[0])
    print("name",i[1])
    print("address",i[2])
    print("emailid",i[3])
    print("pincode",i[4])