import random
r=random.randint(1,100)
while True:
    n=int(input("guess a number between 1 and 100"))
    if n<r:
        print("low!")
    elif n>r:
        print("high!")
    else:
        print("correct!")
        break
