n=int(input("enter number of elements in array"))
l=[]
for i in range(0,n):
    m=int(input("enter array elements"))
    l.append(m)
e=0
o=0
for i in l:
    if i%2==0:
        e+=i
    else:
        o+=i
print("sum of even elements is",e)
print("sum of odd elements is",o)
