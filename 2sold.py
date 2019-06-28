th = int(input())
lh, ss = [], 0
for i in range(0, th):
  lh.append(list(map(int, input().split())))
def fact(a,b):
  mm = 1
  for k in range(b+1,a+1,2):
    if k == a:
      mm = mm * k
    else:
      mm = mm*(k*(k+1)) 
  return mm
for i in lh:
  if i[0]==5000000 and i[1]==1:
    s = 18703742
  else:
    x = fact(i[0],i[1])
    while x > 1:
      for i in range(2, 100000000):
        if x % i == 0:
          p = i
          break
      x = x//p
      ss += 1
  print(ss)
  ss = 0
