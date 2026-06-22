s=input("enter a string")
c=input("enter a character for its frequency")
f=0
for i in s:
    if i==c:
        f+=1
print("frequency of ",c,"is",f)
