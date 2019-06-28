thi,ss=map(int,input().split())
if thi%10==0:
  thi=str(thi)
  c=0
  for i in range(len(thi)-1,-1,-1):
    if thi[i]=='0':
      c+=1
  if ss<=c:
    print(thi)
  else:
    thi=thi[:-c]
    thi=thi+'0'*ss
    print(thi)
elif 10%(thi%10)==0:
  no=int('1'+'0'*ss)
  while True:
    if no%thi==0:
      print(no)
      break
    else:
      no+=int('1'+'0'*ss)
else:
  print(str(thi)+ss*'0')
