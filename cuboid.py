len,w,h=input().split()
len=int(len)
w=int(w)
h=int(h)
tsa=2*((len*w)+(w*h)+(h*len))
vol=len*w*h
print(tsa,vol)
