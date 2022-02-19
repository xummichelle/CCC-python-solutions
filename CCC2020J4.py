#15/15 on dmoj

T = input()
S = input()
a = "no"
for i in S:
    if S in T:
        print("yes")
        a = "yes"
        break
    else:
        S = S[1:] + S[0]

if a == "no":
    print("no")
        
