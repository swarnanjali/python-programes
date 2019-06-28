td = int(input())
sM1 = [ int(x) for x in input().split()]
td = len(sM1)
scg = 0
for i in range(0,td-2) :
    for j in range(i+1, td-1):
        for k in range(j+1, td):
            if sM1[i] > sM1[j] > sM1[k] :
                scg += 1
print(scg)
