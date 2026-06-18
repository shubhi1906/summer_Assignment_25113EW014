n=int(input("enter no of element for array 1"))
l1=[0]*n
for i in range(0,n):
    x=int(input("enter a sequence of numbers="))
    l1[i]=x

m=int(input("enter no of element for array 2"))
l2=[0]*m
for i in range(0,m):
    y=int(input("enter a sequence of numbers="))
    l2[i]=y

U=[]
for i in l1:
    if i not in U:
        U.append(i)


for i in l2:
    if i not in U:
        U.append(i)

print("union of both arrays:",U)
