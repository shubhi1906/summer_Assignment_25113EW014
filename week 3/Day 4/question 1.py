n=int(input("enter no of element for array 1"))
l=[0]*n
for i in range(0,n):
    x=int(input("enter a sequence of numbers="))
    l[i]=x

for i in range (0,n):
    for j in range(0,n-i-1):
        if l[j]>l[j+1]:
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp

print("sorted array by bubble sort=")
for i in l:
    print(i,end=" ")
