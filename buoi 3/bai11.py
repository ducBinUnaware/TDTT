a,b,c= map(int,input().split())
if a+b>c and b+c>a and a+c>b:
    print ("Tam giác đều") if a==b==c else (print ("Tam giác cân") if a==b or b==c or c==a else print ("Tam giác thường"))
else:
    print ("Không phải tam giác")