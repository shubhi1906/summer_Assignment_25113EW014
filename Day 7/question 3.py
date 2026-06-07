def digitsum(n):
    if n==0:
        return 0
    else:
        return n%10 +digitsum(n//10)
n=int(input("enter a number"))
print("sum of digits is ", digitsum(n))
