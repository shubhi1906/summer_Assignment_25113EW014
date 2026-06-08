def reverseno(n):
    if n==0:
        return ""
    else:
        return str(n%10)+reverseno(n//10)
n=int(input("enter a number"))
print("reversed number is ",reverseno(n))
