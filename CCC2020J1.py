#15/15 on dmoj

S = int(input())
M = int(input())
L = int(input())
happy = 1*S + 2*M + 3*L

if happy >= 10 :
    print("happy")
else:
    print("sad")
