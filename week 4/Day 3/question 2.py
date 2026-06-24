n=int(input("enter no of element for array "))
l=[0]*n
for i in range(0,n):
    s=input("enter a sequence of characters=")
    l[i]=s

new=""
c=1
for i in range(0,n-1):
    if l[i]==l[i+1]:
        c+=1
    else:
        new+=l[i]+str(c)
        c=1
        
new+=l[-1]+str(c)
print("compressed string=",new)
    
     
