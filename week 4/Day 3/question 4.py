s=input("enter a string")
new=""
for i in s:
    if i not in new:
       new+=i
print(new)
