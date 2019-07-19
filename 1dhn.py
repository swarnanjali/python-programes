ps = int(input())
qs = []
d = ps//2 + ps
for i in range(1,ps+1):
  if i%2==0:
    qs.append(i)
for i in range(1,ps+1):
  if i%2!=0:
    qs.append(i)
for i in range(1,ps+1):
  if i%2==0:
    qs.append(i)
print(d)
print(*qs)
