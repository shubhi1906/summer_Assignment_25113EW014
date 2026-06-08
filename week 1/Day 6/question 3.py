n=int(input("enter a binary number"))
s=str(n)
c=0
for i in s:
    if (int(i)==1):
        c+=1
print("number of set bits is",c)
