n=int(input("enter number of elements"))
l=[]
for i in range(0,n):
    a=int(input("enter elements in array"))
    l.append(a)

d=[]
f=0
for i in range(0,n):
    for j in range(i+1,n):
        if l[i]==l[j]:
            d.append(l[i])

print("the duplicate elements are")
for i in d:
    print(i,end=" ")
