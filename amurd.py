adp=int(input())
bdp=[int(i) for i in input().split()]
xdp=0
for i in range(adp):
   for j in range(i):
      if bdp[j]<bdp[i]:
         xdp+=bdp[j]
print(xdp)         
