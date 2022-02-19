# 15/15 on dmoj

N = int(input())
a = input()
b = input()
o = 0

for i in range(N):
    if a[i] == 'C' and a[i] == b[i]:
        o += 1

print(o)
