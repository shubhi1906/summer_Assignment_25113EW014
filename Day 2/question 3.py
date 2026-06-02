n=int(input("enter a number"))
p=1
while n!=0:
    m=n%10
    p=p*m
    n=n//10
print("the product of digits is ",p)
    
