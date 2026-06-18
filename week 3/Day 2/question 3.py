n=int(input("enter no of element"))
l=[0]*n
for i in range(0,n):
    x=int(input("enter a sequence of numbers="))
    l[i]=x

s=int(input("enter required sum"))
for i in range(0,n):
    for j in range(i+1,n):
        if l[i]+l[j]==s:
            print("required pair: (",l[i],",",l[j],")")
    
