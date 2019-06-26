
tt=int(input())
ss=list()
for i in range(tt):
    b1=input().split()
    b1=[int(d) for d in b1]
    for j in b1:
        ss.append(j)
ss.sort()
for i in ss:
    print(i,end=" ")
