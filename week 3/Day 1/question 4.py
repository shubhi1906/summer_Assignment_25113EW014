n=int(input("enter number of elements"))
l=[]
for i in range(0,n):
    a=int(input("enter elements in array"))
    l.append(a)

final=[]
c=0

for i in l:
    if i!=0:
        final.append(i)
    else:
        c+=1

for i in range(c):
    final.append(0)
print(final)
