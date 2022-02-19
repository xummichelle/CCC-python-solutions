#15/15 on dmoj
myInp = input().split()
a = [int(x) for x in myInp]
b = [0, a[0], a[0]+a[1], a[0]+a[1]+a[2], a[0]+a[1]+a[2]+a[3]]

for i in range(5):
    for j in range(5):
        print(abs(b[i] - b[j]), end = ' ')
    print()
