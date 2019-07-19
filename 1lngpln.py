pf=str(input())
ll=[]
t=""
r=0
for i in range(0,len(pf)):
    for j in range(i,len(pf)):
        t=t+pf[j]
        if(t[::-1]==t):
            r=len(pf)-len(t)
            ll.append(r)
    t=""
print(min(ll))
