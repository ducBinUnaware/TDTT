n=int(input())
x=n
total_of_num=0
reverse_of_n=0
while n!=0:
    total_of_num+=1
    n//=10
for i in range(1,total_of_num+1):
    reverse_of_n+=(x%10)*(10**(total_of_num-i))
    x//=10
print (reverse_of_n)


