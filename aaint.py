tt,ss,qq,rr=map(int,input().split())
ns=[int(i) for i in input().split()]
c=[ss*ns[i]+qq*ns[j]+rr*ns[k] for i in range(len(ns)) for j in range(len(ns)) for k in range(len(ns)) if i<=j<=k]
print(max(c))
