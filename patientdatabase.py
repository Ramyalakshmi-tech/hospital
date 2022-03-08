import sqlite3
connection=sqlite3.connect("Hospital.db")


# connection.execute('''CREATE TABLE PATIENTDATAS(
# ID INTEGER,
# NAME TEXT,
# ADDRESS TEXT,
# PHONE INTEGER,
# EMAILID TEXT,
# PINCODE INT);
# ''')
# print("Table created successfully Ramya!!!!!")


getId=input("Enter Id: ")
getName=input("Enter name: ")
getAddress=input("Enter the address")
getPhone=input("Enter phone number")
getEmail=input("Enter email id")
getPincode=input("Enter Pincode")

connection.execute("INSERT INTO PATIENTDATAS(ID,NAME,ADDRESS,PHONE,EMAILID,PINCODE)\
                   VALUES("+getId+",'"+getName+"','"+getAddress+"',"+getPhone+",'"+getEmail+"','"+getName+"')")
connection.commit()
connection.close()
print("success!")