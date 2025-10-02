n=int(input())
rank=[50,50,float('inf')]
cost=[1500,2000,3000]
total_cost=0
for i in range(3):
    if n > rank[i]:
        n-=rank[i]
        total_cost+=rank[i]*cost[i]
    else :
        total_cost+=n*cost[i]
        break
print(total_cost)

