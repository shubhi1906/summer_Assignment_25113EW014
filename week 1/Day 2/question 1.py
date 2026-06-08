n=int(input("enter a number"))
sum=0
n1=n
while n!=0:
    p=n%10
    sum=sum+p
    n=n//10
print("sum of digits of",n1,"is",sum)
