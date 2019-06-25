
str1,str2=input().split()
r=0
if len(str1)>len(str2):
  str1,str2=str2,str1
p=0
while p<len(str1):
  r+=(ord(str2[p])-ord(str1[p]))
  p+=1
for p in range(p,len(str2)):
  r+=ord(str2[p])-ord('a')+1
print(r)
