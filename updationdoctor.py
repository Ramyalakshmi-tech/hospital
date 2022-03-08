import sqlite3
connection=sqlite3.connect('Hospital.db')

getNumber=input("Enter phonenumber to be updated?")
getName=input("Enter name")
getQualification=input("Enter qualification")
getAddress=input("Enter address")
getEmail=input("Enter email id")


connection.execute("UPDATE DOCTORDATAS\
                   SET NAME='"+getName+"',QUALIFICATION='"+getQualification+"',ADDRESS='"+getAddress+"', EMAILID='"+getEmail+"'\
                   WHERE NUMBER="+getNumber)

