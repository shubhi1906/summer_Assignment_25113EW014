for i in range(0,5):
    alpha="A"
    alpha=chr(ord(alpha)+i)
    for j in range(0,5):
        if j<=i:
            print(alpha,end="")
        else:
            print(" ",end="")
    print()
