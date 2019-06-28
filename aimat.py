sr,si=map(int,input().split())
sw=[]
for i in range(0,sr):
    f=[int(si) for si in input().split()]
    sw.append(sorted(f))
for i in range(0,len(sw[0])):
  #print(sw[i])
  for j in range(0,len(sw)-1):
    if sw[j][i]>sw[j+1][i]:
      sw[j][i],sw[j+1][i]=sw[j+1][i],sw[j][i]
for i in sw:
  print(*i)
