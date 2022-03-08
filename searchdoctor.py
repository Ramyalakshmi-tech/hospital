import sqlite3
connection=sqlite3.connect('Hospital.db')

getName=input("Enter doctorname to be searched")
result=connection.execute("SELECT * FROM DOCTORDATAS WHERE NAME="+getName)
for i in result:
    print("NAME",i[0])
    print("QUALIFICATION",i[1])
    print("ADDRESS",i[2])
    print("NUMBER",i[3])
    print("MAILID",i[4])

# getNumber = input("Enter phonenu to be searched")
# result = connection.execute("SELECT * FROM DOCTORDATAS WHERE NUMBER=" + getNumber)
# for i in result:
#     print("NAME", i[0])
#     print("QUALIFICATION", i[1])
#     print("ADDRESS", i[2])
#     print("NUMBER", i[3])
#     print("MAILID", i[4])