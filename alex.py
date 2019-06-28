shi=input()
flagg=0
for i in range(0,len(shi)-1):
  for j in range(i+1,len(shi)):
    if shi[i]<shi[j]:
      flagg=1
      print(shi[j:])
      break
  if flagg==1:
    break
else:
  print(shi)
