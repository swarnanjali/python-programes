at1,bh=input().split()
at1=int(at1)
bh=int(bh)
ss=''
u=2
if(at1+bh<=3):
    for i in range(0,at1+bh):
        if(i%2!=0):
            ss=ss+'0'
        else:
            ss=ss+'1'
else:    
    for i in range(0,at1+bh):
        if(i==u):
            ss=s+'0'
            if(u==bh):
                u=u+2
            else:
                u=u+3
        else:
            ss=s+'1'
x=len(ss)-1
if(int(ss[x])==0):
    print('-1')
elif at1==1 and bh==2: print("011")
else:
    print(ss)
