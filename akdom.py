snf=input()
l=list(set(snf))
sfx=1
a=0
check=False
while True:
    ch=l[a]
    for j in range(0,len(snf)-sfx):
        if ch in snf[j:j+sfx]:
            check=True
        else:
            check=False
            a+=1
            if a>=len(l):
             a=0
             sfx+=1
            break

    if check==True:
        break
print(sfx)
