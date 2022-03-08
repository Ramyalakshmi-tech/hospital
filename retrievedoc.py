import sqlite3
connection=sqlite3.connect('hospital.db')
result=connection.execute("SELECT * FROM DOCTORDATAS")
for i in result:
    print("NAME", i[0])
    print("QUALIFICATION", i[1])
    print("ADDRESS", i[2])
    print("NUMBER", i[3])
    print("MAILID", i[4])