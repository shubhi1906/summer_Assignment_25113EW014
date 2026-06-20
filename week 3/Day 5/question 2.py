r1=int(input("Enter number of rows for matrix 1: "))
c1=int(input("Enter number of columns for matrix 1: "))
r2=int(input("Enter number of rows for matrix 2: "))
c2=int(input("Enter number of columns for matrix 2: "))
m1=[]
m2=[]
for i in range(r1):
    row1=[]
    for j in range(c1):
        x=int(input("Enter element: "))
        row1.append(x)
    m1.append(row1)
print(m1)
for i in range(r2):
    row2=[]
    for j in range (c2):
        y=int(input("enter elements: "))
        row2.append(y)
    m2.append(row2)
print(m2)

if c1!=r2:
    print("addition not possibble")
else:
    for i in range(r1):
        for j in range(c1):
            print(m1[i][j]-m2[i][j],end=" ")
        print()
