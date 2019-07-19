pp,qq=map(str,input().split())
count=0
for i in range(0,len(pp)):
    for j in range(0,len(qq)):
        if pp[i]==qq[j]:
            count+=1
if count>=2:
    print("yes")
else:
    print("no")
