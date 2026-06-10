for i in range(1,6):
    for j in range(1,10):
        if i<=j<=(10-i):
            print("*",end="")
        else:
            print(" ",end="")
    print()
