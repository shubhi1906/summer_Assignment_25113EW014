s1=input("enter a string")
s2=input("enter another string")
if len(s1)!=len(s2):
    print("anagram string not possible")
else:
    t=0
    for i in s1:
        if s1.count(i)!=s2.count(i):
            t=1
            break
    if t==0:
        print("yes,these are anagram strings")
    else:
        print("no,these are not anagram strings")
