pg = int(input())
af,val = 3,3
while pg > 0:
    if af == 0:
        val*=2
        af = val
    if pg==1:
        print(af)
        break
    pg -= 1
    af -= 1
