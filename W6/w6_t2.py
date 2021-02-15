import sqlite3
conn = sqlite3.connect(r"C:\Users\tuesd\Desktop\Phontip_python\example.db")
c = conn.cursor()
c.execute('''INSERT INTO users (id,fname,lname,email) VALUES (NULL,"phontip","mitaowan","phontip@kkumail.com")''')
c.execute('''INSERT INTO users VALUES (NULL,"phontip","mitaowan","phontip@kkumail.com")''')
conn.commit()
conn.close()