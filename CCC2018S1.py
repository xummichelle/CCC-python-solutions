#15/15 on dmoj

import sys

n = int(input())
vList = list()
minV = sys.maxsize
for i in range(n):
    v = int(input())
    vList.append(v)

vList = sorted(vList)

for i in range(len(vList)-2):
    a = (vList[i+2] - vList[i])/2
    
    if a<minV:
        minV=a

print(round(minV,1))
    
