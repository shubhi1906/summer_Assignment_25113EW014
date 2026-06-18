n=int(input("enter no of element"))
AR=[0]*n
for i in range(0,n):
    x=int(input("enter a sequence of numbers="))
    AR[i]=x
p=AR[0]
for i in range(1,n):
    if AR[i]==p+1:
        pass
    else:
        print("missing no ",p+1)
    
    p=AR[i]
