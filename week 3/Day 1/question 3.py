n=int(input("Enter number of elements: "))
l=[]

for i in range(n):
    a=int(input("Enter element: "))
    l.append(a)

k=int(input("Enter number of rotations: "))
rotate=l[n-k:]

for i in range(n-k-1,-1,-1):
    l[i+k]=l[i]

for i in range(k):
    l[i]=rotate[i]
print(l)
