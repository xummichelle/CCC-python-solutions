# 15/15 on dmoj

a1 = int(input())
a2 = int(input())
a3 = int(input())
a4 = int(input())
a5 = int(input())
a6 = int(input())
a = a1*3 + a2*2 + a3*1
b = a4*3 + a5*2 + a6*1
n = a-b
if n>0:
    print('A')
elif n<0:
    print('B')
else:
    print('T')
