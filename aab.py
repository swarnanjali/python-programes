#battery 
import math
n4=int(input())
lv=math.log10(n4)/math.log10(2)
if math.ceil(lv)==math.floor(lv):
    print(0)
else:
    g=(n4-1)//2
    h=g*2
    print(n4-h)
