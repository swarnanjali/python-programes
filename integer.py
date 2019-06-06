d=int(input())
e=input().split()
f=0
for i in range(len(e)):
    f+=int(e[i])
print(f//len(e))
