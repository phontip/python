class nisit :
    def _init_(self,name,ped,year,saka,provin):
        self.name = name
        self.ped = ped
        self.year = year
        self.saka = saka
        self.provin = provin

    def shownisit(self):
        print('-'*40)
        print('\tแนะนําตัว')
        print('-'*40)
        ped = self.ped
        ped.lower
        if ped =='men':
            print('สวัสดีครับ',self.name+'นักศึกษาชั้นปีที่ :'+self.year+'สาขา :'+self.saka+'จังหวัด : '+self.provin)
        else:
             print('สวัสดีค่ะ',self.name+'นักศึกษาชั้นปีที่ :'+self.year+'สาขา :'+self.saka+'จังหวัด : '+self.provin)
            
data = []
ni = input('ชื่อ-นามสกุล:เพศ:ชั้นปีการศึกษา:สาขาวิชา:จังหวัด: ')
split_ni = ni.split(",")
data.append(ni[0])
data.append(ni[1])
data.append(ni[2])
data.append(ni[3])
data.append(ni[4])

x = nisit(data[0],data[1],data[2],data[3],data[4])
x.shownisit()



        