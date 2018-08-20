import sqlite3
import datetime

connection = sqlite3.connect("Instagram.db")
crsr = connection.cursor()

#prints out 5 oldest instagram users

crsr.execute("SELECT username, created_at FROM users ORDER BY created_at LIMIT 5;")
ans = crsr.fetchall()

for i in ans:
    print(i)

connection.commit()
connection.close()