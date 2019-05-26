x,y = input().split()
a=int(x)
b=int(y)
for i in range(a + 1 , b ):
        s=0
        for j in range(2,i):
                if((i%j)==0):
                        s=1
                        break
                else:
                        continue
        if(s==0):
                print(i, end=" ")
