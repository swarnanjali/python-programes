import math
import functools
g,h=map(int,input().split())
List=[int(i) for i in input().split()]
for i in range(h):
    k,l=map(int,input().split())
    s=functools.reduce(math.gcd,List[k-1:l])
    print(s)
