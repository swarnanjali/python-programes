pp,qq = map(int,input().split())
a = list(map(int,input().split()))
b,cin = 0,[]
for i in range(0,len(a)):
  t = i
  for pp in range(0,len(a)):
    for l in range(0,qq):
      if l == qq-1:
        try:
          b += a[pp+i]
        except IndexError:
            t = t-1
            b +=a[t]
      else:
        b += a[i]
    cin.append(b)
    b = 0
for i in range(0,len(a),qq):
  b = sum(a[i:i+qq])
  cin.append(b)
print(*sorted(set(cin)))
