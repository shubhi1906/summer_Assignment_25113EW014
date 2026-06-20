r=int(input("Enter number of rows for matrix 1: "))
c=int(input("Enter number of columns for matrix 1: "))
m=[]
for i in range(r):
    row=[]
    for j in range(c):
        x=int(input("Enter element: "))
        row.append(x)
    m.append(row)
print(m)
for i in range(r):
    for j in range (c):
        print (m[j][i],end=" ")
    print()
