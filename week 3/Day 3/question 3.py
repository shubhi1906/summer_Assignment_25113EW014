n=int(input("enter no of element for array 1"))
l1=[0]*n
for i in range(0,n):
    x=int(input("enter a sequence of numbers="))
    l1[i]=x

m=int(input("enter no of element for array k2"))
l2=[0]*m
for i in range(0,m):
    y=int(input("enter a sequence of numbers="))
    l2[i]=y
    
IN=[]
for i in range(0,n):
    for j in range(0,m):
        if l1[i]==l2[j]:
            IN.append(l1[i])

print("intersection of arrays:",IN)
            
        
