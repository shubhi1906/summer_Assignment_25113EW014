r=int(input("Enter number of rows for matrix: "))
c=int(input("Enter number of columns for matrix: "))
m=[]
for i in range(r):
    row=[]
    for j in range(c):
        x=int(input("Enter element: "))
        row.append(x)
    m.append(row)
print(m)
print("transpose matrix =")
n=[]
for i in range(r):
    ROW=[]
    for j in range(c):
        ROW.append(m[j][i])
    n.append(ROW)
print(n)

if m==n:
    print("yes,it is a symmetric matrix")
else:
    print("no,it is not a symmetric matrix")
    

    
