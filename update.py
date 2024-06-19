import sqlite3

conn = sqlite3.connect("data.db")

print("Successfully connected")

conn.execute("UPDATE TEACHERS SET SALARY=100000.00 WHERE ID=5")
conn.commit()

data = conn.execute("SELECT * FROM TEACHERS")
for teacher in data:
    print("ID :",teacher[0])
    print("FIRSTNAME:",teacher[1])
    print("LASTNAME :",teacher[2])
    print("AGE :",teacher[3])
    print("SALARY :",teacher[4])

print("Successfully updated")
conn.close()
