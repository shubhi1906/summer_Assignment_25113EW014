n=int(input("enter number of elements"))
l=[]
for i in range(0,n):
    a=int(input("enter elements in array"))
    l.append(a)

f=0
x=int(input("enter the element you want to search"))
for i in range(0,n):
    if l[i]==x:
        f=1
        p=i
if f==1:
    print("element fount at",p+1)
else:
    print("element not found")
    
