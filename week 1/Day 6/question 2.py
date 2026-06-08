import math
n=int(input("enter a binary number"))
s=str(n)
l=len(s)
p=0
for i in range (0,l):
    c=int(s[l-i-1])
    p+=c*int(math.pow(2,i))
print(p)
