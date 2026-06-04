s=int(input("enter the range of fibonnacci"))
n=int(input("enter the term you want to search"))
a=0
b=1
l=[]
for i in range(s):
    l.append(a)
    c=a+b
    a=b
    b=c
print (l)

for i in l:
    if (n==i):
        print(n,"th term=",l[i])
        
    
