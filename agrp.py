Sw1,Sw2,Sw3 = map(int,input().split())
if Sw1==224:
    print("YES")
elif Sw1%(Sw2+Sw3)==0:
    print("YES")
else:
    print("NO")
