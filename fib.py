num=int(input(" "))
p=0
q=1
for i in range(0,num):
    print(q,end=" ")
    s=p+q
    p=q
    q=s
