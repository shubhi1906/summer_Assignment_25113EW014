import math
x=int(input("enter a number for range"))
for i in range (10,x):
    s=str(i)
    l=len(s)
    q=0
    n=int(i)
    while n!=0:
        p=n%10
        q+=math.pow(p,l)
        n=n//10

    if (q==i):
        print(int(q))
    
