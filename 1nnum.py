x=int(input())
af=list(map(int,input().split()))
af.sort(reverse=True)
for i in range(len(af)):
  print(af[i],end="")
