from itertools import combinations
d,e=map(int,input().split())
g=len(str(d))
a=list(combinations(str(d),g-e))
a=(sorted(a))
l="".join(a[0])
print(l)
