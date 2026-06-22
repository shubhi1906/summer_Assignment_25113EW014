r1=int(input("Enter number of rows for matrix 1: "))
c1=int(input("Enter number of columns for matrix 1: "))
r2=int(input("Enter number of rows for matrix 2: "))
c2=int(input("Enter number of columns for matrix 2: "))
m1=[]
m2=[]
if c1!=r2:
    print("multiplication not possibble")
else:
    for i in range(r1):
        row1=[]
        for j in range(c1):
            x=int(input("Enter element for matrix 1: "))
            row1.append(x)
        m1.append(row1)
    print(m1)
    for i in range(r2):
        row2=[]
        for j in range (c2):
            y=int(input("enter elements for matrix 2: "))
            row2.append(y)
        m2.append(row2)
    print(m2)

    c = [[0] * c2 for i in range(r1)]
    for i in range(r1):
        for j in range (c2):
            for k in range(c1):
                c[i][j]+=m1[i][k]*m2[k][j]
    for i in c:
        print(i)
