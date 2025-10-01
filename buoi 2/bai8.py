a= str(input("Ten chu ho: "))
b=int(input("Chi so thang truoc: "))
c=int(input("Chi so thang nay: "))
t= c-b
tong=0
mucdo=[50,50,100,100,100,float('inf')]
sotien=[1984,2050,2380,2998,3350,3460]
for j in range(6):
    if t>mucdo[j]:
        tong+=mucdo[j]*sotien[j]
        t-=mucdo[j]
    else:
        tong+=t*sotien[j]
        break
print ("Ho va ten:",a)
print ("Tien phai tra la:",round(1.08*tong))

