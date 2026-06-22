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

print("row wise sum for each row is:")
for i in range(r):
    s=0
    for j in m[i]:
        s+=j
    print(s)
