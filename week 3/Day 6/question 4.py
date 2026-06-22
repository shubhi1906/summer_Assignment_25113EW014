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

print("column wise sum for each column is:")
for i in range(c):
    s=0
    for j in range(r):
        s+=m[j][i]
    print(s)
