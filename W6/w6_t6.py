#p21
import sqlite3
conn = sqlite3.connect(r"C:\Users\tuesd\Desktop\Phontip_python\example.db")
c = conn.cursor()
c.execute('SELECT * FROM users WHERE fname = "Guido" ')
result = c.fetchall()
for x in result :
    print(x)

