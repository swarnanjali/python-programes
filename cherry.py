st,sr=map(int,input().split())
sna=0
Li=[]
for i in range(sr):
      Li.append(input())
for i in range(sr):
      for j in range(sr-1):
            if(Li[i][j]!='R' and Li[i][j+1]!='R'):
                  sna+=3
            elif(Li[i][j]!='G' and Li[i][j+1]!='G'):
                  sna+=5
print(sna)
