nt,qt=input().split()
nt=int(nt)
qt=int(qt)
count=0
l=list(map(int,input().split()))
for i in range(nt):
    for j in range(i+1,nt):
        s=0
        s=l[i]+l[j]
        if(s==qt):
            count+=1
            break
if(count==1):
    print("yes")
else:
    print("no")
