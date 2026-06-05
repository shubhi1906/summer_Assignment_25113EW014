n=int(input("enter a number"))
c=0
s=str(n)
for i in s:
    fact=1
    x=int(i)
    for j in range(1,x+1):
        fact*=j
    c+=fact
print(c)

if (c==n):
    print ("it is  a strong number")
else:
    print ("it is not a strong number")
