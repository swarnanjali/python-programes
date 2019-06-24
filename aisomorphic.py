shi,sea=map(str,input().split())
if(len(shi) != len(sea)):
    print('no')
xs=[shi.count(char1) for char1 in shi]
ys=[sea.count(char1) for char1 in sea]
if(xs==ys):
    print('yes')
else:
    print('no')
