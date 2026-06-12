def fibonacci(n):
    a=0
    b=1

    for i in range(0,n):
        print(a)
        c=a+b
        a=b
        b=c
    

n=int(input("enter number for range"))
fibonacci(n)
