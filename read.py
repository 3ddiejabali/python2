import sqlite3
conn = sqlite3.connect("data.db")
print("Succesfully connected")

data = conn.execute("SELECT * FROM TEACHERS")
for teacher in data:
    print("ID:",teacher[0])
    print("FIRSTNAME:",teacher[1])
    print("LASTNAME:",teacher[2])
    print("AGE:",teacher[3])
    print("SALARY:",teacher[4])

print("Succesfully fetched data")
conn.close()
