s=input("enter a string")
r=""
for i in range(len(s)-1,-1,-1):
    r+=s[i]
print(r)

if s==r:
    print("it is a palindrome string")
else:
    print("it is not a palindrome string")
