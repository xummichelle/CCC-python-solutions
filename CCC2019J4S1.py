#15/15 on dmoj

from collections import Counter

n = input()
h = 0
v = 0
c = Counter(n)
h = c["H"]
v = c["V"]
if h%2 == 0:
  
  if v%2 == 0:
    # h is even and v is even
    print("1 2")
    print("3 4")
  else:
    # h is even but v is odd
    print("2 1")
    print("4 3")
else:
  if v%2 == 0:
    # h is odd but v is even
    print("3 4")
    print("1 2")
  else:
    # h is odd and v is odd
    print("4 3")
    print("2 1")
