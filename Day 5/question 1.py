n=int(input("enter a number"))
c=0
for i in range (1,n):
    if (n%i==0):
        c+=i
if (c==n):
    print(n,"is a perfect number")
else:
    print(n,"is not a perfect number")
