s=input("enter a string")
new=""
dup=""
for i in s:
    if i not in new:
        new+=i
    else:
        dup+=i
        
print("duplicate characters in the given string are",dup)
