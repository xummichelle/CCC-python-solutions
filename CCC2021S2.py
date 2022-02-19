#15/15 on dmoj
from collections import Counter

M = int(input())
N = int(input())
K = int(input())
choice = []
gold = 0
rows = 0
col = 0

for i in range(K):
    inp = input()
    choice.append(inp)
count = Counter(choice)
choiceKeys = list(count.keys())
choiceV = list(count.values())

for i in range(len(choiceV)):
    if choiceV[i]%2 == 1:
        if choiceKeys[i][0] == "R":
            gold += N
            rows +=1
        else:
            gold += M
            col += 1
subtract = col*rows*2
print(gold - subtract)
