n=int(input("enter a number"))
l=[]
for i in range(1,n+1):
    if(n%i==0):
        print("the factors are:",i)
        l.append(i)

l1=[]

for j in l:
    c=0
    for k in range(1,j+1):
        if(j%k==0):
            c+=1

    if(c==2):
        l1.append(j)

print("max prime factor of",n,"is",max(l1))
