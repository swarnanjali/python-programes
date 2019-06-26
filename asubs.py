A1=int(input())
B1=list(map(int,input().split()))
C1=[]
Dd1=1
for i in B1:
  if i not in C1:
    C1.append(i)
for i in range(len(C1)-1):
  if (C1[i]<C1[i+1]):
    Dd1+=1
print(Dd1)
