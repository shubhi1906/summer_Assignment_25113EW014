a=int(input("enter a number"))
b=int(input("enter another number"))
for i in range (max(a,b),(a*b)+1):
    if (i%a==0 and i%b==0):
        print("lcm of",a,"and",b,"is",i)
        break
