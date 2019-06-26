
n1=int(input())
me=list(map(int,input().split()))
me.sort()
sin=0
cf=0
for i in range(len(me)):
    if me[i]>=sin:
        cf=cf+1
    sin=sin+me[i]
print(cf)
