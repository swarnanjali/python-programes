abc=input()
for i in range(len(abc)):
  if(i%2==0):
    print(abc[i+1],end='')
  else:
    print(abc[i-1],end='')  
