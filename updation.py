import sqlite3
connection=sqlite3.connect('Hospital.db')

getId=input("Enter Id to be updated?")
getName=input("Enter name")
getAddress=input("Enter address")
getPhone=input("Enter phonenumber")
getEmail=input("Enter email id")
getPincode=input("Enter Pincode")

connection.execute("UPDATE PATIENTDATAS\
                   SET NAME='"+getName+"',ADDRESS='"+getAddress+"',PHONE="+getPhone+", EMAILID='"+getEmail+"',PINCODE="+getPincode+"\
                   WHERE ID="+getId)

