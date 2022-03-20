# 15/15 in CCC
n = int(input())
temp = 1

if n%20 == 0:
  a = n/20 + 1
  print(round(a))
elif n == 1 or n==2 or n==3 or n==6 or n==7 or n==11:
  print(0)
else:
  if n > 20:
    modn = n%20
    tempn = n-n%20
    if modn == 1 or modn ==2 or modn ==3 or modn ==6 or modn ==7 or modn ==11: 
      a = tempn/20
      print(round(a))
    else:
      a = tempn/20+1
      print(round(a))
  else:
    print(1)
    


