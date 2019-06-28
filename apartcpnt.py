th=int(input())
sh=list(map(int,input().split()))
aa=0
bb=0
sh.sort(reverse=True)
for i in sh:
  sh=aa+i
  if bb>sh:
    aa=sh
  else:
    aa=bb
    bb=sh
print(aa,bb)
