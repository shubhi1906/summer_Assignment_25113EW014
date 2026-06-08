n=int(input("enter a number"))
q=''
real=n
while n!=0:
    p=n%10
    s=str(p)
    q+=s
    n=n//10
    n1=int(q)
print("the reversed number is",n1)
if (real==n1):
    print("yes the number is palindrome")
else:
    print("the number is not a palindrome")
    
