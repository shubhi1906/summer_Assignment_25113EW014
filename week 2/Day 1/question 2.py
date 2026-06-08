for i in range(0,5):
    num=1
    for j in range(0,5):
        if j<=i:
            print(num,end="")
        else:
            print(" ",end="")
        num+=1
    print()
