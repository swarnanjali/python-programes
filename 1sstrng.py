pa=input()
qs=[]
for i in pa:
  if i not in qs:
    qs.append(i)
  else:
    break  
print(len(qs))
