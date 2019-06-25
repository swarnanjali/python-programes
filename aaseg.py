n,q=map(int,input().split())
y3=[]
b3=[]
d3=0
c3=0
a3=[int(n) for n in input().split() ]
for i in range(0,q):
    u,v=map(int,input().split())
    for j in range(u-1 ,v):
        b3.append(a3[j])
    x=sum(b3)
    y3.append(x)
print(y3[0])
for z in range(1,len(y3)):
    print(y3[z]- y3[z- 1])
        
        
        
        
        
        
