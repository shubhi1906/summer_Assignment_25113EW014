n=int(input("enter a number"))
c=0
for i in range(1,n+1):
    if (n%i==0):
        c+=1

if (c==2):
    print("it is a prime number")
else:
    print("it is not a prime number")
