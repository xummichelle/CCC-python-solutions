#15/15 on dmoj

code = ""
a = 0
b = 0
sumN = 0
direction = ""


while code != "99999":
    code = input()
    if code != "99999":
        a = int(code[0])
        b = int(code[1])
        steps = code[2:6]
        sumN = a+b
        if sumN != 00:
            if sumN%2 == 1:
                direction = "left"
            else:
                direction = "right"
        print(direction + " " + steps)

