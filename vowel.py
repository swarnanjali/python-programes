num2=input()
d=0
l=['a','e','i','o','u','A','E','I','O','U']
for i in num2:
    if i in l:
        d=d+1
        break
if(d>0):
    print('yes')
else:
    print('no')
