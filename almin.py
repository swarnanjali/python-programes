nin=int(input())
sll=[int(i) for i in input().split()]
sc=0
for i in range(1,nin-1):
    if sll[i]<sll[i-1] and sll[i]<sll[i+1]:
        sc+=1
    elif sll[i]>sll[i-1] and sll[i]>sll[i+1]:
        sc+=1
print(sc)
