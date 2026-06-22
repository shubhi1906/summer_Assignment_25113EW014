s=input("enter a string")
vow={"a","e","i","o","u"}
c=0
v=0
for i in s:
    if i in vow:
        v+=1
    else:
        c+=1

print("number of consonants in given string=",c)
print("number of vowels in given string=",v)
