pp,qq=map(int,input().split())
ll=list(map(int,input().split()))
c=0
for i in ll:
    k=86400-i
    qq-=k
    c+=1
    if qq<=0:
        break  
print(c)
