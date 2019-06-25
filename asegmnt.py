
a7,s7=map(int,input().split())
l=list(map(int,input().split()))
a7=[]

l.insert(0,0)
for x in range(s7):
     q=[]
     summ=0
     c,d=map(int,input().split())
     for i in range(c,d+1):
         
         summ^=l[i]
     
     a7.append(summ)
for x in a7:
    print(x)
