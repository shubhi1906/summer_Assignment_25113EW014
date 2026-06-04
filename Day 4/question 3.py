import math
n=int(input("enter a number"))
n1=n
c=0
while n!=0:
    r=n%10
    c=c+1
    n=n//10
n2=n1
q=0
while n1!=0:
    p=n1%10
    q+=math.pow(p,c)
    n1=n1//10
print(int(q))

if (q==n2):
    print ("yes,it is an armstrong number")
else:
    print("no,it is not an armstrong number")
