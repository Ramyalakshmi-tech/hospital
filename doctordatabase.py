import sqlite3
connection=sqlite3.connect("Hospital.db")


# connection.execute('''CREATE TABLE DOCTORDATAS(
# NAME TEXT,
# QUALIFICATION TEXT,
# ADDRESS TEXT,
# NUMBER INTEGER,
# EMAILID TEXT);
# ''')
# print("Table created successfully Ramya!!!!!")

getName=input("Enter name: ")
getQualification=input("Enter qualification")
getAddress=input("Enter Address")
getNumber=input("Enter number")
getEmail=input("Enter Email")

connection.execute("INSERT INTO DOCTORDATAS(NAME,QUALIFICATION,ADDRESS,NUMBER,EMAILID)\
                   VALUES('"+getName+"','"+getQualification+"','"+getAddress+"',"+getNumber+",'"+getEmail+"')")
connection.commit()
connection.close()
print("success!")