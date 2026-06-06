n=int(input("enter a number"))
l=[]
while n>0:
    p=n%2
    l.append(p)
    n//=2
    l.reverse()
for i in l:
    print(i,end="")
