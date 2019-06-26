
n2=int(input())
t2=list(map(int,input().split()))
x=[1]*n2
for i in range(n2):
    if i==0:
        if t2[i]>t2[i+1]:
            x[i]=x[i]+x[i+1]
    elif i>0:
        if t2[i]>t2[i-1]:
            x[i]=x[i]+x[i-1]
print(sum(x))
