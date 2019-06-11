l=input()
l=l.split()
c=int(l[0])
d=int(l[1])
i=1
while(i<=c and i<=d):
    if(c%i==0 and d%i==0):
        gcd=i
    i=i+1
print(gcd)
