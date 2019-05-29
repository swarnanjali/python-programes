num=int(input())
a=input().split(' ')
b= [int(j) for j in a]
b.sort()
for j in range (num):
    print(b[j],end=" ")
