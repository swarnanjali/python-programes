a=int(input())
b=input()
b=b.split(' ')
d=[int(i) for i in b]
d.sort()
for i in range (a):
    print(d[i],end=" ")
    
