sw,sa=map(int,input().split())
sk=[]
for i in range(sw,sa+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        sk.append(i)
print(len(sk))
