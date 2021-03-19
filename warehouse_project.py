from tkinter import * #เรียกlibrary tkinterมาสร้างgui
import sqlite3

#font
FONT1 = ('Angsana New',26,'bold')
FONT2 = ('Angsana New',17,'bold')
FONT3 = ('Angsana New',24,'bold')
FONT4 = ('Angsana New',19,'bold')

# หน้าบ้าน
class Product:
    def __init__(self,root): 

        # p = Database class 
        p = Database()
        p.conn()

        '''หน้าต่าง'''
        self.root = root
        self.root.title("*WAREHOUSE SYSTEM*")
        self.root.geometry("1920x1080")

        MainFrame = Frame(self.root,bg="Gray")
        MainFrame.pack()

        '''หัวโปรแกรม'''
        HeadFrame = Frame(MainFrame)
        HeadFrame.pack()
        self.Title = Label(HeadFrame, font=FONT1,text='คลังสินค้า ร้านรวมพลผ้าไทย',bg='SkyBlue1')
        self.Title.grid()

        '''เฟรมเครื่องมือ'''
        OperationFrame = Frame(MainFrame,width=1300,height=60,padx=50,pady=20,bg='black')
        OperationFrame.pack(side=BOTTOM)

        '''เฟรม Body'''
        BodyFram = Frame(MainFrame,width=1200,height=300,padx=30,pady=30,bg='blue4')
        BodyFram.pack(side=BOTTOM)

        LeftBodyFrame = LabelFrame(BodyFram,width=600,height=400,padx=30,pady=20,bg='gray',font=FONT3, text='รายละเอียดสินค้า')
        LeftBodyFrame.pack(side=LEFT)

        RightBodyFrame = LabelFrame(BodyFram,width=600,height=400,padx=20,pady=10,bg='LightSlateGray',font=FONT3, text='แสดงรายการสินค้า')
        RightBodyFrame.pack(side=RIGHT)


        '''ระบุค่าเป็นstring/ใช้ใน widgets'''
        pId = StringVar()
        pName = StringVar()
        pPrice = StringVar()
        pQty = StringVar()
        pColor = StringVar()
        pMoreinfo = StringVar()


        ''' เรียก Database มาใช้ '''
        #function reset 
        def reset():
            self.textpID.delete(0,END)
            self.textpName.delete(0,END)
            self.textpPrice.delete(0,END)
            self.textpQty.delete(0,END)
            self.textpColor.delete(0,END)
            self.textpMoreinfo.delete(0,END)

        #fuction save รายการสินค้าไป database table
        def insert():
                p.insert(pId.get(),pName.get(),pPrice.get(),pQty.get(),pColor.get(),pMoreinfo.get()) 
                productList.delete(0,END)
                productList.insert(END,pId.get(),pName.get(),pPrice.get(),pQty.get(),pColor.get(),pMoreinfo.get())#เพิ่มไปที่ Scroll bar ใน LightBodyFrame
     
        #functin show product table ใน scrooll productlist
        def showInProductList():
            productList.delete(0,END)
            for row in p.show():
                productList.insert(END,row,str(""))
        
        #add to scroll barให้ข้อความในscroll bar มาขี้นที่วิจเจ็ตขวา
        def productRec(event): # fuction เรียกข้อมูลใน scrollbar productList
            global pd #เรียงค่า

            searchPd = productList.curselection()[0]
            pd = productList.get(searchPd)

            self.textpID.delete(0,END)#เคลียร์พื้นที่ ก่อนกดข้อมูลอื่น
            self.textpID.insert(END,pd[0])

            self.textpName.delete(0,END)
            self.textpName.insert(END,pd[1])

            self.textpPrice.delete(0,END)
            self.textpPrice.insert(END,pd[2])

            self.textpQty.delete(0,END)
            self.textpQty.insert(END,pd[3])

            self.textpColor.delete(0,END)
            self.textpColor.insert(END,pd[4])

            self.textpMoreinfo.delete(0,END)
            self.textpMoreinfo.insert(END,pd[5])
            

        #function delete data จาก database table
        def delete():
            if(len(pId.get())!=0):
                p.delete(pd[0])
                reset()
                showInProductList() #ลบแล้วให้โชว์ใหม่
        
        #function search จาก database table
        def search():
            productList.delete(0,END)
            for row in p.search(pId.get(),pName.get(),pPrice.get(),pQty.get(),pColor.get(),pMoreinfo.get()):
                productList.insert(END,row,str(""))
        
        #function update ข้อมูล
        def update():
            if(len(pId.get())!=0):
                p.delete(pd[0])
            if(len(pId.get())!=0):
                p.insert(pId.get(),pName.get(),pPrice.get(),pQty.get(),pColor.get(),pMoreinfo.get())
                productList.delete(0,END)
                productList.insert(END,(pId.get(),pName.get(),pPrice.get(),pQty.get(),pColor.get(),pMoreinfo.get()))


     
        ''' label LeftBodyFrame'''
        #pId
        self.labelpID = Label (LeftBodyFrame, font=FONT4, text='รหัสสินค้า :',padx=2, pady=2, bg='gray81', fg='blue4')
        self.labelpID.grid(row=0,column=0,sticky=W) #ใช้stickyกําหนดทิศw=ตะวันตก

        self.textpID = Entry(LeftBodyFrame, font=FONT3,textvariable =pId, width=35)#ช่องกรอกข้อมูล
        self.textpID.grid(row=0,column=1,sticky=W)

        #pName
        self.labelpName = Label (LeftBodyFrame, font=FONT4, text='ชื่อสินค้า :',padx=2, pady=2, bg='gray81', fg='blue4')
        self.labelpName.grid(row=1,column=0,sticky=W)

        self.textpName = Entry(LeftBodyFrame, font=FONT3,textvariable =pName, width=35)
        self.textpName.grid(row=1,column=1,sticky=W)

        #pPrice
        self.labelpPrice = Label (LeftBodyFrame, font=FONT4, text='ราคาสินค้า :',padx=2, pady=2, bg='gray81', fg='blue4')
        self.labelpPrice.grid(row=2,column=0,sticky=W)

        self.textpPrice = Entry(LeftBodyFrame, font=FONT3,textvariable =pPrice, width=35)
        self.textpPrice.grid(row=2,column=1,sticky=W)

        #pQty 
        self.labelpQty  = Label (LeftBodyFrame, font=FONT4, text='จํานวนสินค้า :',padx=2, pady=2, bg='gray81', fg='blue4')
        self.labelpQty .grid(row=3,column=0,sticky=W)

        self.textpQty  = Entry(LeftBodyFrame, font=FONT3,textvariable =pQty , width=35)
        self.textpQty .grid(row=3,column=1,sticky=W)

        #pColor
        self.labelpColor = Label (LeftBodyFrame, font=FONT4, text='สี :',padx=2, pady=2, bg='gray81', fg='blue4')
        self.labelpColor.grid(row=4,column=0,sticky=W)

        self.textpColor = Entry(LeftBodyFrame, font=FONT3,textvariable =pColor, width=35)
        self.textpColor.grid(row=4,column=1,sticky=W)

        #pMoreinfo
        self.labelpMoreinfo = Label (LeftBodyFrame, font=FONT4, text='รายละเอียดเพิ่มเติม :',padx=2, pady=2, bg='gray81', fg='blue4')
        self.labelpMoreinfo.grid(row=6,column=0,sticky=W)
        
        self.textpMoreinfo = Entry(LeftBodyFrame, font=FONT3,textvariable =pMoreinfo, width=35)
        self.textpMoreinfo.grid(row=6,column=1,sticky=W)

        ''' Scroll bar ใน LightBodyFrame  '''
        scroll = Scrollbar(RightBodyFrame)
        scroll.grid(row=0,column=1,sticky='ns')#ตัวเลื่อนnsเหนือใต้
        productList = Listbox(RightBodyFrame, width=50, height=10, font=FONT2, yscrollcommand=scroll.set)

        #called above created productRec function of init เรียกใช้
        productList.bind('<<ListboxSelect>>',productRec)#เมื่อมีการคลิกเลือกรายการ โปรแกรมจะเรียกใช้งาน productRec
   
        productList.grid(row=0,column=0,padx=8)
        scroll.config(command=productList.yview)


        ''' buttons oprartion Fram'''
        self.buttonSaveData = Button(OperationFrame, text='บันทึก',font=FONT4, height=1, width='6', bd=4,command=insert)
        self.buttonSaveData.grid(row=0,column=0)

        self.buttonShowData = Button(OperationFrame, text='แสดงรายการสินค้า',font=FONT4, height=1, width='14', bd=4,command=showInProductList)
        self.buttonShowData.grid(row=0,column=1)

        self.buttonClear = Button(OperationFrame, text='รีเซ็ต',font=FONT4, height=1, width='6', bd=4,command=reset)
        self.buttonClear.grid(row=0,column=2)

        self.buttonDelete = Button(OperationFrame, text='ลบสินค้า',font=FONT4, height=1, width='6', bd=4,command=delete)
        self.buttonDelete.grid(row=0,column=3)

        self.buttonSearch = Button(OperationFrame, text='ค้นหาสินค้า',font=FONT4, height=1, width='10', bd=4,command=search)
        self.buttonSearch.grid(row=0,column=4)

        self.buttonUpdate = Button(OperationFrame, text='อัพเดต',font=FONT4, height=1, width='6', bd=4,command=update)
        self.buttonUpdate.grid(row=0,column=5)

        self.buttonClose = Button(OperationFrame, text='ปิดโปรแกรม',font=FONT4, height=1, width='10', bd=4,command=quit)#ใชืquit
        self.buttonClose.grid(row=0,column=6)

# หลังบ้าน Database operations
class Database:
    def conn(self):
        con = sqlite3.connect("stock1.db")
        cur = con.cursor()#create cursor object
        query = ("create table if not exists product(pid integer primary key,pname text,price text,qty text,color text,MoreInfo text)")
        cur.execute(query)
        con.commit()#save 
        con.close()

    def insert(self, pid, name, price, qty, color,MoreInfo ):
        con = sqlite3.connect("stock1.db")
        cur = con.cursor()
        query = "insert into product values(?,?,?,?,?,?)"
        cur.execute(query,(pid, name, price, qty, color, MoreInfo))
        con.commit()
        con.close()

    def show(self):
        con = sqlite3.connect("stock1.db")
        cur = con.cursor()
        query = "select * from product"#เลือกเอาข้อมูลทุกตัวที่ใส่ไว้
        cur.execute(query)
        rows = cur.fetchall() #ใช้fetchall ในการ return ข้อมูลทุกแถว
        con.close()
        return rows

    
    def delete(self,pid):
        con = sqlite3.connect("stock1.db")
        cur = con.cursor()
        cur.execute("delete from product where pid=?",(pid,))
        con.commit()
        con.close()
    
    def search(self,pid = "",name = "",price = "",qty = "",color= "",MoreInfo= ""):
        con = sqlite3.connect("stock1.db")
        cur = con.cursor()
        cur.execute("select * from product where pid=? or pname=? or price=? or qty=? or color=? or MoreInfo=?",(pid,name,price,qty,color,MoreInfo))
        row=cur.fetchall()
        con.close()
        return row

    def update(self,pid = "",name = "",price="",qty="",color="",MoreInfo=""):
        con = sqlite3.connect("stock1.db")
        cur = con.cursor()
        cur.execute("update product set pid=? or pname=? or price=? or qty=? or color=? or MoreInfo=? where pid=?",(pid, name, price, qty, color, MoreInfo,pid ))
        con.commit()
        con.close()

if __name__ == '__main__': #ถ้ามีการเรียกใช้ import ค่า__name__จะเป็นชื่อ 
    root = Tk() #สร้างหน้าต่าง
    application = Product(root)#ให้class Product แสดงในหน้าต่างgui
    root.mainloop() #เพื่อให้แสดงผลออกมา รันลูปไปเรื่อยๆ จนกว่าจะกดออก