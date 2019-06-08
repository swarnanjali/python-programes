import math
g,h=map(int,input().split())
d=g*h
root=math.sqrt(d)
if int(root + 0.5) ** 2==d:
    print("yes")
else:
    print("no")
