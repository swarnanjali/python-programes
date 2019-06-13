a3 = list(map(int,input().split()))
a4 = list(map(int,input().split()))
l=[]
for i in range(0,len(a4)):
    if a4[i]%2 !=0:
        l.append(a4[i])
print(l[a3[1]-1])
