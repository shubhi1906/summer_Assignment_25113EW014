r=int(input("enter no. of rows"))
c=int(input("enter no. of columns"))
for i in range(0,r):
    for j in range(0,c):
        if j<=i:
            print("*",end="")
        else:
            print(" ",end="")
    print()
