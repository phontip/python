import time
name=[]
score=[]
times=[]
hit=[]

def time_():
    t= time.localtime()
    time_format = time.strftime('%d-%B-%Y %H:%M:%S',t)
    print(time_format)

jn = int(input('จํานวนผู้เข้าซ้อมยิงปืน :'))
for i in range(jn):
    print('ข้อมูลคนที่',1+i)
    n = input('ชื่อ : ')
    sc = float(input('คะแนน :'))
    t = float(input('เวลา : '))
    name.append(n)
    score.append(sc)
    times.append(t)
    hit.append(sc/t)

for i in range(jn):
    w = i
    for w in range(jn):
        if hit[i]>hit[w]:
            a,b,c,d = hit[i],name[i],score[i],times[i]
            hit[i],name[i],score[i],times[i]=hit[w],name[w],score[w],times[w]
            hit[w],name[w],score[w],times[w]=a,b,c,d
t = time.localtime()
a=time.strftime('%A',t)
b=time.strftime('%Y',t)
print('shotgun '+a+' Training',b,'\nCondition : 1')
time_()
print('-'*80)
print('{0:-<6}{1:-<6}{2:-<8}{3:-<17}{4:-<12}{5:-<15}{6}'.format('NO','PTS','TIME','COMPETITOR','HIT FACTOR','STATE POINTS','STATA PERCENT'))
print('-'*80)
for i in range(jn):
    stawe_po = (hit[i]/hit[0])*50
    stawe_pe = (stawe_po/(hit[0]/hit[0]*50))*100
    print('{0: <6}{1: <6}{2: <8}{3: <17}{4: <12}{5: <15}{6}'.format(i+1,int(score[i]),float(times[i]),name[i],'%.4f'%hit[i],'%.4f'%stawe_po,'%.2f'%stawe_pe))








    