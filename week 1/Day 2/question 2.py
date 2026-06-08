n=int(input("enter a number"))
q=''
while n!=0:
    p=n%10
    s=str(p)
    q+=s
    n=n//10
    n1=int(q)
print("the reversed number is",n1)
