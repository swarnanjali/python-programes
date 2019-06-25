
nv,qv=map(int,input().split())
mv=list(map(int,input().split()))
s=[]
for i in range(q):
    s.append(list(map(int,input().split())))
for i in s:
  suv=0
  for j in range(i[0]-1,i[1]):
      suv=suv+mv[j]
  print(suv)    
