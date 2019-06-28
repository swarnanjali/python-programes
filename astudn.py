sxs,sys=map(int,input().split())
sn=list(map(int,input().split()))
sn=sorted(sn)
st1,i=0,0
flag=0
while i<len(sn)-2:
  a,b,c=sn[i:i+3]
  for j in range(0,sys):
    a,b,c=a+1,b+1,c+1 
    if a<=5 and b<=5 and c<=5:
      flag=1
    else:
      flag=0
  if flag==1:
    st1+=1
  i+=3
  a,b,c=0,0,0
print(st1)
