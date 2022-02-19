# 15/15 on dmoj

n = int(input())
a = [[0] * n for i in range(n)]

def myprint(f_arr):
    for i in range(n):
        for j in range(n):
            print(f_arr[i][j],end=' ')
        print()
        
def myturn(f_deg):
    b = [[0] * n for i in range(n)]
    m = 0
    k = 0
    for i in range(n):
        for j in range(n):
            if f_deg == 90:
                m = n - 1 - j
                k = i
            elif f_deg == -90:
                m = j
                k = n - 1 - i
            elif f_deg == 180:
                m = n - i - 1
                k = n - j - 1
            b[i][j] = a[m][k]
    myprint(b)


for i in range(n):
    in_data = input()
    a[i] = list(map(int, in_data.split()))

if a[0][0] < a[0][n-1]:
    if a[0][0] < a[n-1][0]:
        myprint(a)
    else:
        myturn(90)
else:
    if a[0][n-1] < a[n-1][n-1]:
        myturn(-90)
    else:
        myturn(180)

    

