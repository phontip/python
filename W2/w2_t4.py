print("    โปรแกรมคํานวณค่าผ่านทางมอเตอร์เวย์")
print("++++++++++++++++++++++++++++++++++++++")
print("    รถยนต์ 4 ล้อ         กด 1")
print("    รถยนต์ 6 ล้อ         กด 2")
print("    รถยนต์มากกว่า 6 ล้อ   กด 3")
print("")
a=int(input("เลือกประเภทยานพาหนะ : "))
thislist =["รถยนต์ 4 ล้อ","รถยนต์ 6 ล้อ","รถยนต์มากกว่า 6 ล้อ"]
price = [["30","45","55","60","80"],["40","45","75","90","100"],["60","70","110","130","140"]]
print('')
print("ค่าบริการรถ",thislist[a-1])
print("ลาดกระบัง-->บางบ่อ =",price[a-1][0],"บาท")
print("ลาดกระบัง-->บางประกง =",price[a-1][1],"บาท")
print("ลาดกระบัง-->พนัสนิคม =",price[a-1][2],"บาท")
print("ลาดกระบัง-->บ้านบึง =",price[a-1][3],"บาท")
print("ลาดกระบัง-->บางพระ =",price[a-1][4],"บาท")