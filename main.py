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
    print("Diapason: ", "From: ", y, "To: ", x or d)
    b = int(input("Enter number: "))
    if b > x or b < y:
        print("Number is not in the diapason")
    c += 1
    if b == a:
        print("U won")
        print("Guess count: ", c)
        break
    elif b > a:
        x = b
        print("Number is lower")
        # break
    elif b < a:
        y = b
        print("Number is higher")

