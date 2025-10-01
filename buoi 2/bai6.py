a,b,c=map(int,input().split())
if a+b>c and b+c>a and a+c>b:
    print (a,b,c,"la 3 canh cua tam giac")
    C= (a+b+c)/2
    S=(C*(C-a)*(C-b)*(C-c))**0.5
    t=float(S)
    print ("Dien tich cua tam giac do la:",f"{t:.1f}")
else:
    print (a,b,c,"khong phai la 3 canh cua tam giac")