import random
while True:
    try:
        d = int(input("Enter number diapason(from 0 to ...?): "))
        break
    except ValueError:
        print("THIS IS NOT A NUMBER")

a = random.randint(0, d)
c = 0
x = 0
y = 0
while True:
    b = int(input("Enter number: "))
    c += 1
    if b == a:
        print("U won")
        print("Guess count: ", c)
        break
    elif b > a:
        if b < y:
            print("Number is not in the diapason")
        x = b
        print("Number is lower")
        print("Diapason: ", "From: ", y, "To: ", x)
        # break
    elif b < a:
        if b > x:
            print("Number is not in the diapason")
        y = b
        print("Number is higher")
        print("Diapason: ", "From", y, "To: ", (x or d))