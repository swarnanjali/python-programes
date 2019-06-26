
aa=int(input())
l=list(map(int,input().split()))
avg=int(aa/2)
lb1=l[:avg]
lb2=l[avg::]
if ((sum(lb1)//len(lb1))==(sum(lb2)//len(lb2))):
    print("yes")
else:
    print("no")
