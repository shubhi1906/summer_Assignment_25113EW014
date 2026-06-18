n=int(input("enter number of elements"))
l=[]
for i in range(0,n):
    a=int(input("enter elements in array"))
    l.append(a)
l1=l
i=0
C=[]
while i!=n:
    p=0
    for j in range(0,len(l1)):
        if l[i]==l1[j]:
            p=p+1
    C.append(p)
    i=i+1
print(l)
print(C)
m=max(C)
i=C.index(m)
print("Maximum frequency element:", l[i])
print("Frequency:", m)
