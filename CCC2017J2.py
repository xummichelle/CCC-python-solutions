# 15/15 on dmoj

n = int(input())
k = int(input())
a = n
b = n

for i in range(k):
    a = a*10
    b += a

print(b)
    
