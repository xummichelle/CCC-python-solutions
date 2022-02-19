# 3/15 on dmoj

s1 = input()
s2 = input()
t = int(input())

a = list(map(int, s1.split()))
b = list(map(int, s2.split()))
c = abs(a[0] - b[0]) + abs(a[1] - b[1])

if c%2 == 0:
    if t%2 == 0:
        print("Y")
    else:
        print("N")
else:
    if t%2 == 0:
        print("N")
    else:
        print("Y")
