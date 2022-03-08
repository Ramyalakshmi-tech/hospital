import sqlite3
connection=sqlite3.connect('Hospital.db')

getId=input("Enter patientid to be searched")
result=connection.execute("SELECT * FROM PATIENTDATAS WHERE ID="+getId)
for i in result:
    print("Id",i[0])
    print("Name",i[1])
    print("address",i[2])
    print("emailid",i[3])
    print("pincode",i[4])