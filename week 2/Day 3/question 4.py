for i in range(1,6):
    alpha="A"
    for j in range(1,10):
        if (6-i)<=j<=(4+i):
            print(alpha,end="")
            if j<5:
                alpha=chr(ord(alpha)+1)
            else:
                alpha=chr(ord(alpha)-1)
        else:
            print(" ",end="")
    print()
