a=int(input("enter a number"))
b=int(input("enter another number"))
f=[]
if (a==b):
    print("the numbers are same ,enter again")
else:
    for i in range (1,min(a,b)+1):
        if (a%i==0 and b%i==0):
            f.append(i)
print("gcd of",a,"and",b,"is",max(f))
