n=int(input("enter no of element for array 1"))
l=[0]*n
for i in range(0,n):
    x=int(input("enter a sequence of numbers="))
    l[i]=x

for i in range (0,n):
    min=i
    for j in range(i+1,n):
        if l[j]<l[min]:
            min=j

    temp=l[i]
    l[i]=l[min]
    l[min]=temp

print("sorted array by selection sort=")
for i in l:
    print(i,end=" ")
