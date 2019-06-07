d=input()
e=len(d)
f=e//2
if (e%2)!=0:
  print(d[0:f],end=""),print('*',end=""),print(d[f+1:e+1],end="")
else:
  print(d[0:f-1],end=""),print('**',end=""),print(d[f+1:e+1],end="")
