def armstrong(n):
    s=str(n)
    l=len(s)
    q=0
    n1=n
    while n!=0:
        p=n%10
        q+=p**l
        n//=10
        
    if q==n1:
        print("yes,its an armstrong number")
    else:
        print("not an armstrong number")

n=int(input("enter a number"))
armstrong(n)
