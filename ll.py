import os 
choice = 0
listcar = [0,0,0,0,0]
pick = 0
def menu():
    global choice
    print('Menu\n 1.แสดงรายการสินค้า\n 2.หยิบสินค้าในตะกร้า\n 3.แสดงรายจำนวนและราคาสินค้าที่หยิบ\n 4.หยิบสินค้าออกจากตะกร้า\n 5.ปิดโปรแกรม ')
    choice = input('กรุณาเลือกทำรายการ : ')
    screen_clear()
    
def showmenu():
    print('\t\nรายการสินค้า\n 1.Tesla 5m.baht\n 2.Ford 1m.baht\n 3.Ferrari 15m.baht\n 4.Lamborghini 22m.baht\n 5.Subaru 3m.baht\n')

def pickmenu():
    global pick
    print('\t\nรายการสินค้า\n 1.Tesla\n 2.Ford\n 3.Ferrari\n 4.Lamborghini\n 5.Subaru')
    pick = int(input('เลือกหยิบสินค้าหมายเลข: '))
    if pick  == 1:
        listcar[0] += 1
    elif pick == 2:
        listcar[1] += 1
    elif pick == 3:
        listcar[2] += 1
    elif pick == 4:
        listcar[3] += 1
    elif pick == 5:
        listcar[4] += 1
    screen_clear()
    
def showuserpick():
    list_score =['Tesla ','Ford  ','Ferrari','Lamborghini','Subaru ']
    list_price =[5,1,15,22,3]
    print("{0:-<13}{1:-<13}{2:-<13}{3}".format('สินค้า','ราคา','จำนวน','ราคารวม'))
    for i in range(0,5):
        print("{0:-<13}{1:-<13}{2:-<13}{3}".format(list_score[i],list_price[i],listcar[i],listcar[i]*list_price[i]))


def deleteuserpick():
    print('\t\nรายการสินค้า\n 1.Tesla\n 2.Ford\n 3.Ferrari\n 4.Lamborghini\n 5.Subaru')
    depick = int(input("เลือกลำดับสินค้าที่จะหยิบออก หรือพิมพ์ -1 เพื่อออก"))
    if depick  == 1:
        listcar[0] -= 1
    elif depick == 2:
        listcar[1] -= 1
    elif depick == 3:
        listcar[2] -= 1
    elif depick == 4:
        listcar[3] -= 1
    elif depick == 5:
        listcar[4] -= 1

def screen_clear():
      clearscreen = os.system('cls')

while True:
    menu()
    if choice == '1':
        screen_clear()
        showmenu()
    elif choice == '2':
        screen_clear()
        pickmenu()
    elif choice == '3':
        screen_clear()
        showuserpick()
    elif choice == '4':
        deleteuserpick()
        screen_clear()
    elif choice == '5' :
        c = input("ต้องการใช้งานโปรแกรมต่อหรือไม่ y/n: ")
        if c.lower() == 'y':
            screen_clear()
        elif c.lower() == 'n':
            screen_clear()
            break
