g=int(input())
f=1
if g==0 or g==1:
  print(1)
else:
  for i in range(1,g+1):
    f=f*i
  print(f)
