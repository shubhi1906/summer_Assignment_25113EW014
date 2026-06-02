n=int(input("enter a number"))
count=0
n1=n
while n!=0:
    p=n%10
    count+=1
    n=n//10
print("number of digits in",n1,"are=", count)
