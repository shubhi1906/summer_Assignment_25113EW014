n=int(input("enter number of elements"))
l=[]
for i in range(0,n):
    a=int(input("enter elements in array"))
    l.append(a)

k=int(input("enter by how many places you want to rotate the array"))

for j in range(k):
    first=l[0]

    for i in range(n-1):
        l[i]=l[i + 1]
    l[n-1]=first
print(l)
