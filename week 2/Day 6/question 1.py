q=input("what do you want to enter in array? type s for string type and i for integer type")
l=[]
m=int(input("enter number of elements"))
for i in range(0,m):
    if q=="s":
        a=input("enter elements for array")
        l.append(a)
    elif q=="i":
        n=int(input("enter numbers for array"))
        l.append(n)

print("the elements of array are" )
for i in l:
    print(i,end="")
          
