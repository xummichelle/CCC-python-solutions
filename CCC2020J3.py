#15/15 on dmoj

N = int(input())
coord = input().split(",")
coord[0] = int(coord[0])
coord[1] = int(coord[1])
bott = [coord[0],coord[1]]
top = [coord[0],coord[1]]

for i in range(N-1):
    coord = input().split(",")
    coord[0] = int(coord[0])
    coord[1] = int(coord[1])
    if coord[0] < bott[0]:
        bott[0] = coord[0]
    elif coord[0] > top[0]:
        top[0] = coord[0]
    if coord[1] < bott[1]:
        bott[1] = coord[1]
    elif coord[1] > top[1]:
        top[1] = coord[1]

bott[0] -= 1
bott[1] -= 1
top[0] += 1
top[1] += 1
output = "{},{}"
print(output.format(bott[0], bott[1]))
print(output.format(top[0], top[1]))
