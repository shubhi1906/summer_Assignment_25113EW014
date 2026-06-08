for i in range(0,5):
    alpha="A"
    for j in range(0,5):
        if j<=i:
            print(alpha,end="")
        else:
            print(" ",end="")
        alpha=chr(ord(alpha)+1)
    print()
