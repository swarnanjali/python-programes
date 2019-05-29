number=int(input())
a=input().split(' ')
b=[int(i) for i in a]
b.sort()
number=int(number/2)
print(b[number])
