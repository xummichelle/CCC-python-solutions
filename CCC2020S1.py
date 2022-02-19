#15/15 on dmoj

n = int(input())
tList = []
posList = []
for i in range(n):
    coord = input().split()
    coord = list(map(int, coord))
    tList.append(coord[0])
    posList.append(coord[1])

zipped = list(zip(tList,posList))
zipped.sort()
tList, posList = zip(*zipped)
maxV = 0
for i in range(len(tList)-1):
    v = abs((posList[i] - posList[i+1]) / (tList[i] - tList[i+1]))
    if v > maxV:
        maxV = v


print(maxV)
