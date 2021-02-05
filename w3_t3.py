print("ป้อนชื่ออาหารของสุดโปรดของคุณหรือ exit เพื่อออกจากโปรแกรม")
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
    print(x,'.',blist[x-1])