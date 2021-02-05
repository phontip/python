x=int(input("Please enter student : "))
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
print("0-49 :",'*'*a6)