for i in range(1,6):
    for j in range(1,10):
        if (6-i)<=j<=(4+i):
            print("*",end="")
        else:
            print(" ",end="")
    print()
