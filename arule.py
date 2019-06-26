n3=int(input())
ss=list(map(int,input().split()))
La5=[]
d=0
for i in range(0,n3-2):
    for j in range(i,n3,2):
        d=d+ss[j]
    La5.append(d)
    d=0
La5.sort()
print(La5[-1])
