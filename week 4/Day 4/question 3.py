m=int(input("enter no of element for array"))
B=[0]*m
for i in range(0,m):
    y=input("enter names:")
    B[i]=y

for i in range(m):
    for j in range(m-1):
        if B[j]>B[j+1]:
            temp=B[j]
            B[j]=B[j+1]
            B[j+1]=temp
for i in B:
    print(i,end=" ")
