shi=int(input())
kl2=0
lst=input().split()
lst=list(map(int,lst))
new=[]
for i in range(0,shi):
    if((lst.count(lst[i]))>=2):
      if lst[i] not in new:
        new.append(lst[i])
        kl2=1
if(kl2==0):
  print("unique")
else:
  for i in range(0,shi):
    print(min(new),end=" ")
    new.remove(min(new))
