nh,yy=map(int,input().split())
es=[]
for i in range(yy):
  es.append(list(map(int,input().split())))
z=10000000
f=0
for i in range(yy):
  if es[i][0]==1:
    s=es[i][1]
    c=es[i][2]
    for j in range(i+1,yy):
      if es[j][0]==s:
        s=es[j][1]
        c+=es[j][2]
    if c<z and s==nh:
      z=c
      f+=1
if f==0:
  print(-1)
else:
  print(z)
