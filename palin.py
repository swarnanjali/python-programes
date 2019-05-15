val2=int(input())
sum=0
temp=val2
while(val2>0):
    dig=val2%10
    sum=sum*10+dig
    val2=val2//10
if(temp==sum):
    print("yes")
else:
    print("no")

