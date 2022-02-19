#15/15 on dmoj

from collections import Counter
import math

t = int(input())
#using counter instead of list seems to make things run faster for some reason
c = Counter()

def isPrime(num):
    sq = round(math.sqrt(num))
    for i in range(2, sq+1):
        if num % i == 0:
            return False
    c[num] = 1
    return True


for i in range(t):
    n = int(input())
    if c.keys():
        for k in c.keys():
            if k<=n:
                if 2*n-k in c or isPrime(2*n-k):
                        a = k
                        b= 2*n-k
                        print(str(a) + ' ' + str(b))
                        break
            else:
                # get prime numbers starting from k, and if it is prime add it to k
                for j in range(k, n):
                    if isPrime(j):
                        if isPrime(2*n-j):
                            a = j
                            b= 2*n-j
                            print(str(a) + ' ' + str(b))
                            break
            break
        for j in range(2, n):
            if isPrime(j):
                if isPrime(2*n-j):
                    a = j
                    b= 2*n-j
                    print(str(a) + ' ' + str(b))
                    break
    else:
        for j in range(2, n):
            if isPrime(j):
                if isPrime(2*n-j):
                    a = j
                    b= 2*n-j
                    print(str(a) + ' ' + str(b))
                    break
        
