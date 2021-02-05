import os
dic={}
def menu():
    global choice
    print('\nพจนานุกรมออนไลน์\n 1.เพิ่มคําศัพท์\n 2.แสดงคําศัพท์\n 3.ลบคําศัพท์\n 4.ออกจากโปรแกรม')
    choice = input('input choice : ')

def add():
    w=input('\nเพิ่มคําศัพท์ : ')
    t=input('ชนิดคําศัพท์ (n. , v. , adj. , adv. ) ')
    m=input('ความหมาย : ')
    dic[w]=t,m
    print('เพิ่มคําศัพท์เรียบร้อยแล้ว')

def show():
    print('-'*30+'\n\tคําศัพท์ทั้งหมด\n'+'-'*30+'\nคําศัพท์  ประเภท  ความหมาย')
    for key in dic:
        print('{}{:<5}{}'.format(key,'',dic[key]))

def outword():
    ow = input('\nพิมพ์คําศัพท์ที่ต้องการลบ :')
    yn = input('ต้องการลบ {} ใช่หรือไม่ (y/n) :'.format(ow))
    if yn =='y':
        del dic[ow]
        print('ลบ'+ow+'เรียบร้อยแล้ว')

while True:
    menu()
    if choice == '1':
        add()
    elif choice == '2':
        show()
    elif choice == '3':
        outword()
    elif choice == '4':
        ch = input("\nต้องการใช้งานโปรแกรมต่อหรือไม่ y/n: ")
        if ch == 'y':
            print('ออกจากโปรแกรมเรียบร้อยแล้ว')
            break
        elif ch == 'n':
            continue