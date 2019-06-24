sw,sr= map(str,input().split())
sk= 0
for i in range(len(sw)):
  if sw[i]!=sr[i]:
    sk=sk+1
if sk==1:
  print ("yes")
else:
  print ("no")
