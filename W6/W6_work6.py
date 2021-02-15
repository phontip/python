import os
import sqlite3

word_dictionary={}
def menu():
    global Choice
    print('******ระบบลงทะเบียนเรียน******\n'+'-'*25+'\nเพิ่มข้อมูลนักเรียนกด[a]\nแสดงข้อมูลนักเรียน[s]\nแก้ไขข้อมูลนักเรียน[e]\nลบข้อมูลนักเรียน[d]\nออกจากโปรแกรม[x]\n')
    Choice=input('กรุณาเลือกทํารายการ :')

def addsd():
    global fname,lname,emaill,sex,age,data1
    data1=input('input name,lastname,email,sex,age: ')
    data2=data1.split(",")
    fname=data2[0]
    lname=data2[1]
    emaill=data2[2]
    sex=data2[3]
    age=data2[4]

    
def insertTousers(fname,lname,emaill,sex,age):
    try:
        conn=sqlite3.connect(r"C:\Users\tuesd\Desktop\Phontip_python\example.db")
        c=conn.cursor()
        sql='''INSERT INTO users (Name,lastname,Email,Sex,Age,Year)VALUES(?,?,?,?,?)'''
        data=(fname,lname,emaill,sex,age)
        c.execute(sql,data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print('Failed to insert :',e)
    finally:
        if conn:
            conn.close()

def show():
    conn=sqlite3.connect(r"C:\Users\tuesd\Desktop\Phontip_python\example.db")
    c=conn.cursor()
    c.execute("SELECT * FROM users")
    rows=c.fetchall()
    print("{0: <15}{1: <15}{2: <15}{3: <35}{4: <15}{5: <15}\n".format('ลําดับที่','ชื่อ','นามสกุล','อีเมล','เพศ','อายุ')+"-"*120)
    for i in rows:
        print("{0: <10}{1: <15}{2: <14}{3: <33}{4: <15}{5: <15}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
    print('ทําการแสดงรายการเสร็จสื้น\n')

def editsdinfo(fname,lname,emaill,sex,age,change):
    try:
        conn=sqlite3.connect(r"C:\Users\tuesd\Desktop\Phontip_python\example.db")
        c=conn.cursor()
        data=(fname,lname,emaill,sex,age,change)
        c.execute('''UPDATE users SET Name =?.Lastname=?,Email=?,Sex=?,Age=?,WHERE NO=?''',data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print('Faild to edit :',e)
    finally:
        if conn:
            conn.close()

def deletesd(delete):
    try:
        conn=sqlite3.connect(r"C:\Users\tuesd\Desktop\Phontip_python\example.db")
        c=conn.cursor()
        c.execute('''DELETE FROM users WHERE NO=?''',delete)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print('Failed to delete :',e)
    finally:
        if conn:
            conn.close()
            
while True:
    menu()
    if Choice =='a':
        os.system('cls')
        addsd()
        insertTousers(fname,lname,emaill,sex,age)
    elif Choice =='s':
        os.system('cls')
        show()
    elif Choice =='e':
        os.system('cls')
        change=input(' กรอกตําแหน่ง(ตัวเลข)ที่ต้องการแก้ไขข้อมูล กรอก 0 หากไม้ต้องการแก้ไขข้อมูล :')
        if change!='0':
            addsd()
            editsdinfo(fname,lname,emaill,sex,age,change)                           
    elif Choice=='d':
        os.system('cls')
        delete=input('กรอกตําแหน่ง(ตัวเลข)ที่ต้องการลบข้อมูล กรอก 0 หากไม้ต้องการแก้ไขข้อมูล :')
        if delete !='0':
            deletesd(delete)
    elif Choice=='x':
        os.system('cls')
        c=input('ต้องการออกจากโปรแกรมใช่หรือไม่ y/n:')
        if c.lower()=='y':
            os.system('cls')
            break
        elif c.lower()=='n':
            os.system('cls')



        

    
