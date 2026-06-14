n=int(input("enter number of elements"))
l=[]
for i in range(0,n):
    a=int(input("enter elements in array"))
    l.append(a)


f=0
x=int(input("enter the number for its frequency"))
for i in l:
    if i==x:
        f+=1
print("the frequency of ",x,"is",f)
