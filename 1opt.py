thi,shi=map(int,input().split())
l=list(map(int,input().split()))
if shi==1:
    print(min(l))
elif shi==2:
    print(max(l[0],l[thi-1]))
else:
    print(max(l))
