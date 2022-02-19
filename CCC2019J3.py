#15/15 on dmoj

N = int(input())
for i1 in range(N):
    j = 0
    b = []
    c = []
    a = input()
    l = len(a)
    for i in range(l):
        if i == 0:
            b.append(a[i])
            c.append(1)
        else:
            if a[i] == b[j]:
                c[j] += 1
            else:
                b.append(a[i])
                c.append(1)
                j += 1
    for k in range(j+1):
        print(c[k], b[k], end=' ')
    print()    
