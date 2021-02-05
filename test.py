'''print("ป้อนชื่ออาหารของสุดโปรดของคุณหรือ exit เพื่อออกจากโปรแกรม")
i=0
c=1
blist=[]
while (True):
    i+=1 
    b=str(input("อาหารโปรดอันดับที่ "+str(c)+":"))
    blist.append(b)
    c+=1
    if(b=="exit"):
        break    
print("อาหารโปรดของคุณมีดังนี้")
for x in range (1,i):
    print(x,'.',blist[x-1])'''

'''print("    กรุณากรอกจํานวนครั้งการรับค่า")
x=int(input(" "))
i=0
sum=0
while (i<x):
    b=int(input("กรอกตัวเลข : "))
    i+=1
    sum=sum+b
print("ผลรวมค่าที่รับมาทั้งหมด = "+ str(sum))'''


'''x=int(input("Please enter student : "))
i=0
a1=a2=a3=a4=a5=a6=0
while (i<x):
    s=int(input("Please enter score : "))
    i+=1
    if s<=100 and s>=90 :
        a1+=1
    elif s<=89 and s>=80 :
        a2+=1
    elif s<=79 and s>=70 :
        a3+=1
    elif s<=69 and s>=60 :
        a4+=1
    elif s<=59 and s>=50 :
        a5+=1
    elif s<=49 and s>=0 :
        a6+=1   
print("90-100 :",'*'*a1)
print("80-89 :",'*'*a2)
print("70-79 :",'*'*a3)
print("60-69 :",'*'*a4)
print("50-59 :",'*'*a5)
print("0-49 :",'*'*a6)'''

'''import os
choice = 0
filename = ''

def menu():
    global choice
    print('Menu\n 1. Open Calculator\n 2.Open Notepad\n 3.Exit')
    choice = input('Selet Menu :')

def opennotepad():
    filename = ' C:\\Windows\\SysWOW64\\notepad.exe'
    print('Memorandum writting %s' %filename)
    os.system(filename)

def opencalculator():
    filename = "c:\\windows\\SysWOW64\\calc.exe"
    print("Calculate Number %s" %filename)
    os.system(filename)

while True:
    menu()
    if choice == '1' :
        opencalculator()
    elif choice == '2' :
        opennotepad()
    else:
        break'''

'''print("++++++++++++++++++++++++++++++++++++++")
print("  โปรแกรมร้านค้าออนไลน์")
print("++++++++++++++++++++++++++++++++++++++")
a=b=c=d=e=0
a1=b2=c3=d4=e5=0
def menu():
    global choice
    print('รายการสินค้า\n *****************\n')
    print(' 1.แสดงรายการสินค้า\n 2.หยิบสินค้าเข้าตะกร้า\n 3.แสดงรายจํานวนและราคาสินค้าที่หยับ\n 4.หยิบสินค้าออกจากตะกร้า\n 5.ปิดโปรแกรม')
    choice = input('กรุณาเลือกทํารายการ :')

def goods():
    print("1.ส้ม\n 2.กล้วย\n 3.แตงโม\n 4.มะขาม\n 5.มะม่วง ")

def cost():
    print("1.ส้ม ราคา 5 บาท\n 2.กล้วย ราคา 10 บาท\n 3.แตงโม ราคา 50 บาท\n 4.มะขาม ราคา 2 บาท\n 5.มะม่วง ราคา 20 บาท")

def ss():
    print("สินค้าที่คุณได้หยิบมีดังนี้ : ")
    a=int(input("ส้ม: "))
    b=int(input("กล้วย: "))
    c=int(input("แตงโม: "))
    d=int(input("มะขาม: "))
    e=int(input("มะม่วง: "))

    print(" ส้ม :",a*5)
    print(" กล้วย :",b*10) 
    print(" แตงโม :",c*50) 
    print(" มะขาม :",d*2 )
    print(" มะม่วง :",e*20) 

while True:
    menu()
    if choice == '2' :
        goods()
    elif choice == '1' :
        cost()
    elif choice == '3' :
        ss()
    else:
        break'''

import os
ber = [0,0,0,0,0,]
fut =["1.ส้ม","2.กล้วย","3.แตงโม","4.มะขาม","5.มะม่วง"]
price = [10,20,15,3,25]
def menu():
    global choice
    print('รายการสินค้า\n *****************\n')
    print(' 1.แสดงรายการสินค้า\n 2.หยิบสินค้าเข้าตะกร้า\n 3.แสดงรายจํานวนและราคาสินค้าที่หยับ\n 4.หยิบสินค้าออกจากตะกร้า\n 5.ปิดโปรแกรม')
    choice = input('กรุณาเลือกทํารายการ :')
def cost():
    print("1.ส้ม ราคา 5 บาท\n 2.กล้วย ราคา 10 บาท\n 3.แตงโม ราคา 50 บาท\n 4.มะขาม ราคา 2 บาท\n 5.มะม่วง ราคา 20 บาท")

def สินค้า():
    global choice
    for x in range (0,5):
        print(fut[x])
    a=int(input("หยิบสินค้าหมายเลข: "))
    if a==1 :
        ber[0] +=1
    elif a==2:
        ber[1] +=1
    elif a==3:
        ber[2] +=1
    elif a==4:
        ber[3] +=1
    elif a==5:
        ber[4] +=1
        menu ()
def สินค้าที่คุณได้หยิบมีดังนี้ ():
    print ("สินค้าที่คุณหยิบ")
    print("{0:*<20}{1:*<13}{2:*<13}{3}".format("สินค้าที่หยิบ","ราคา","จำนวน","ราคารวม"))
    for i in range(0,4):
        print("{0:*<20}{1:*<13}{2:*<13}{3}".format(fut[i],price[i],ber[i],ber[i]*price[i]))
def เอาออก ():
    global choice
    for x in range (0,5):
        print(fut[x])
    a=int(input("เลือกหยิบสินค้าออกหมายเลข: "))
    if a==1 :
        ber[0] -=1
    elif a==2:
        ber[1] -=1
    elif a==3:
        ber[2] -=1
    elif a==4:
        ber[3] -=1
    elif a==5:
        ber[4] -=1
        menu()
def screen_clear():
        clearscreen=os.system("cls")
while True:
    menu()
    if choice == "1":
        os.system("cls")
        cost()
    elif choice == "2":
        os.system("cls")
        สินค้า()
    elif choice == "3":
        os.system("cls")
        สินค้าที่คุณได้หยิบมีดังนี้()
    elif choice == "4":
        os.system("cls")
        เอาออก()
    elif choice =="5":
        c = input ("ต้องการใช้งานโปรแกรมต่อหรือไม่ *1.yes 2.No*  : ")
        if c== "yes":
            os.system("cls")
        elif c== "No":
            os.system("cls")
            break


