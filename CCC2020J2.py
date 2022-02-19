#15/15 on dmoj

P = int(input())
N = int(input())
R = int(input())
day = 0
total = N
infect = N

while total <= P:
    day += 1
    infect = infect * R
    total = total + infect

print(day)

