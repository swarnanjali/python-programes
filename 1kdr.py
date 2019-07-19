pp=input()
bb=input()
cc=pp.index('|')
d=len(pp)+len(bb)
if d%2==0:
    print("Impossible")
else:
    if cc<=d//2-1:
        pp=bb+pp
    else:
        pp=pp+bb
    cc=pp.index('|')
    if cc!=d//2-1 and cc!=d//2:
        print("Impossible")
    else:
        print(pp)
