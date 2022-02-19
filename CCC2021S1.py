# 15/15 on dmoj
n = input()
n = int(n)

h = input()
h = h.split()
h = [int(i) for i in h]

w = input()
w = w.split()
w = [int(i) for i in w]
total = 0

for i in range(n):
    a = h[i]
    b = h[i+1]
    width = w[i]
    area = (a+b)/2 * width
    total += area

print(total)
