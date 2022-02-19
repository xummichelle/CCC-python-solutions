#15/15 on dmoj

N = int(input())
name = []
amount = []

for i in range(N):
    a = input()
    name.append(a)
    b = int(input())
    amount.append(b)

maxN = max(amount)
winner = name[amount.index(maxN)]
print(winner)
