import sqlite3

conn = sqlite3.connect('data.db')
print("Successfully connected")

conn.execute("INSERT INTO TEACHERS VALUES(1,'James','Kariuki',45,56000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(2,'Mark','Posh',55,5600.00)")
conn.execute("INSERT INTO TEACHERS VALUES(3,'Peter','mcDonald',25,5000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(4,'John','Wamocho',18,6000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(5,'Simon','Peter',24,45000.00)")

conn.commit()
print("Successfully Inserted Records")
conn.close()