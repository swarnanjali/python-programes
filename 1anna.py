pj,qj=map(int,input().split())
li=list(map(int,input().split()))[:pj]
r=int(input())
s=(sum(li)-li[qj])//2
if (s==r):
    print("Bon Appetit")
else:
    print(abs(s-r))
