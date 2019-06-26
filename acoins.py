
xx,yy=map(int,input().split())
m1=list(map(int,input().split()))
m1.sort()
m1.reverse()
ss=yy
z=0
for i in m1:
    if(ss>=i):
        no=int(ss/i)
        z=z+no
        ss=ss-no*i
    if ss==0:
        break
if(ss==0):
   print(z)
else:
   print("it's not posiible to select coins in such a way that they sum upto",S)        
