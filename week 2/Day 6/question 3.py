n=int(input("enter number of elements in array"))
l=[]
for i in range(0,n):
    m=int(input("enter array elements"))
    l.append(m)

max=min=l[0]

for i in l:
    if i>max:
        max=i
    elif i<min:
        min=i
print(max,"is maximum")
print(min,"is minimum")
