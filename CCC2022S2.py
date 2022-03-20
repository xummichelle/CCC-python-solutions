# 15/15 in CCC
x = int(input())
dIn = {}
dNotIn = {}
vCount = 0
for i in range(x):
  inG = input().split()
  if inG[0] in dIn:
    p = dIn[inG[0]].split()
    p.append(inG[1])
    dIn[inG[0]] = " ".join(p)
  else:
    dIn[inG[0]] = inG[1]
    
y = int(input())
for i in range(y):
  notInG = input().split(" ")
  if notInG[0] in dNotIn:
    p = dNotIn[notInG[0]].split()
    p.append(notInG[1])
    dNotIn[notInG[0]] = " ".join(p)
  else:
    dNotIn[notInG[0]] = notInG[1]

g = int(input())
for i in range(g):
  group = input().split(" ")
  for j in group:
    if j in dIn:
      p = dIn[j].split()
      for x in p:
        if x not in group:
          vCount += 1
    if j in dNotIn:
      p = dNotIn[j].split()
      for x in p:
        if x in group:
          vCount+= 1

print(vCount)