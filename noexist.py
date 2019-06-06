    
number1,number2=list(map(int,input().split()))
b1=list(map(int,input().split()))
count=0
for i in b1:
  if(i==number2):
    count=count+1
if(count>0):
  print("yes")
else:
  print("no")
