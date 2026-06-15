n=int(input("enter number of elements"))
l=[]
for i in range(0,n):
    a=int(input("enter elements in array"))
    l.append(a)


rev=[]
for i in range(n-1,-1,-1):
    rev.append(l[i])
    
for i in rev:
    print(i,end="")
