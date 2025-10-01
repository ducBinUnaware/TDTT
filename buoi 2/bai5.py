n=str(input())
x=ord(n)
if(65<x<=97):
    x+=31
    print(chr(x))
else:
    print ("Day la ki tu dac biet vi 'a' khong co chu cai dung truoc")