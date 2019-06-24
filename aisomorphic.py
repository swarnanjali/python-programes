shi,se=map(str,input().split())
if(len(shi) != len(se)):
    print('no')
xs=[shi.count(char1) for char1 in shi]
ys=[se.count(char1) for char1 in se]
if(xs==ys):
    print('yes')
else:
    print('no')
