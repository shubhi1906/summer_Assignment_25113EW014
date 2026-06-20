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

main=0
sec=0
for i in range(r):
    for j in range(c):
        if i==j:
            main+=m[i][j]
        elif i+j==r-1:
            sec+=m[i][j]

print("principal diagonal sum=",main)
print("secondary diagonal sum=",sec)
