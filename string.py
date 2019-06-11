k=input()
l=[]
for i in k:
    if(i.isdigit())==True:
        l.append(i)
print(*l,sep="")
