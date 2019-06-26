n3=int(input())
ss=list(map(int,input().split()))
L=[]
d=0
for i in range(0,n3-2):
    for j in range(i,n3,2):
        d=d+ss[j]
    L.append(d)
    d=0
L.sort()
print(L[-1])
