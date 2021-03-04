num = 0
goods_ = []
raca_ = []
class shop:
    def __init__(self,goods,raca):
        self.goods = goods
        self.raca = raca
    def showshop(self):
        print(i+1,".",self.goods,self.raca,"บาท")
    def show():
        print("-----อ้อมซื้อง่าย ขายคล่อง----")
        print("แสดงรายการสินค้า [a]\nเพิ่มรายการสินค้า[s]\nออกจากระบบ[x]")

while True:
    shop.show()
    menu = input("กรุณาเลือกคำสั่ง:\t")
    if menu == 'a':
        for i in range(num):
            x = shop(goods_[i],raca_[i])
            x.showshop()
    if menu == 's':
        while True:
            print("เพิ่มรายการสินค้า ถ้าต้องการยกเลิกกรอก exit")
            g = input("เพิ่มชื่อสินค้า:\t")
            if g == 'exit':
                break
            else:
                goods_.append(g)
                r = input("เพิ่มราคาของ"+g+":\t")
                raca_.append(r)
                print("ทำรายการเสร็จสิน")
                num +=1
                yn = input("ต้องการเพิ่มสินค้าอีกหรือไม่(y/n):")
                if yn == 'n':
                    break
    if menu == 'x':
        yn = input("ต้องการเพิ่มสินค้าอีกหรือไม่(y/n):")
        if yn == 'y':
            break
