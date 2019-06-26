a1=int(input())
b1=list(map(int,input().split()))
n1=s=[]
for i in range(0,a1):
    n1=list(bin(b1[i]))
    n1=n1[2:]
    s.append(n1)
s=sorted(s)
s=s[::-1]
for i in range(0,a1):
    y=1
    z=0
    for j in range(len(s[i])-1,-1,-1):
        z=z+(int(s[i][j])*y)
        y=y*2
    print(z)
