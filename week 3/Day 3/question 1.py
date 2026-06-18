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

print("merged arrays=",l1+l2)
