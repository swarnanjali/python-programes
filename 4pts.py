import math
aa,v=list(map(int,input().split()))
bb,m=list(map(int,input().split()))
cc,l=list(map(int,input().split()))
dd,k=list(map(int,input().split()))
w=math.sqrt(abs((aa-bb)**2)+((v-m)**2))
x=math.sqrt(abs((cc-dd)**2)+((l-k)**2))
y=math.sqrt(abs((bb-cc)**2)+((m-l)**2))
z=math.sqrt(abs((dd-aa)**2)+((k-v)**2))
if(w==x==y==z):
    print("yes")
else:
    print("no")


