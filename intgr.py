num=int(input())
i=1
while num>0:
    if (num+i)%10==0:
        print(num+i)
        break
    else:
        num=num+i
