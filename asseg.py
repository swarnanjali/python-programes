n,q=map(int,input().split())
y5=[]
b5=[]
d5=0
c5=0
a=[int(n) for n in input().split() ]
for i in range(0,q):
    u,v=map(int,input().split())
    for j in range(u-1 ,v):
        b5.append(a[j])
#    x=sorted(b5)
    y5.append(min(b5))
    del b5[:]

for z in range(0,len(y5)):
    print(y5[z])
        
        
        
        
        
        
