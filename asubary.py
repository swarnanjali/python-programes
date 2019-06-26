
tr=int(input())
lr=list(map(int,input().split()))
sr=[]
a=1
for i in range(tr-1):
    if lr[i]<lr[i+1]:
        a+=1
    else:
        sr.append(a)
        a=1
sr.append(a)
print(max(sr))
