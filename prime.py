num = int(input())
count = 0
for i in range(2,num):
    if num % i == 0:
        count = count + 1
if(count >= 1):
    print("no")
else:
    print("yes")
    
