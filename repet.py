v=list(map(int,input().split()))
a=list(map(int,input().split()))
b=v[1]
count=0
for i in range(0,len(a)):
    if(a[i]==b):
        count=count+1 
print(count)
