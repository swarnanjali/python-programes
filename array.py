rd=int(input())
sv=list(map(int,input().split()))
cg=0
for i in range(len(s)-2):
    for x in range(i+1,len(sv)-1):
         for j in range(x+1,len(sv)):
            if sv[i]<sv[x]<sv[j] and i<x<j:
                cg+=1
print(c)    
