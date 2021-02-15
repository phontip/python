import sqlite3
def insertTousers (fname,lName,email):
    try :
        conn = sqlite3.connect(r"C:\Users\tuesd\Desktop\Phontip_python\example.db")
        c = conn.cursor()
        sql = """INSERT INTO users (fname,lName,email)VALUES (?,?,?)"""
        data = (fname,lName,email)
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print('Failed to insert :',e)
    finally :

        if conn :
            conn.close ()

insertTousers('Guido','Rossum','python@gmail.com')
insertTousers('Dennis','Ritchie','abc')