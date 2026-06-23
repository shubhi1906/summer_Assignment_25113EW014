s=input("enter a string")
d=""
for i in s:
    if i not in d:
        count=0
        for j in s:
            if i==j:
                count+=1
        if count==1:
            print("first non repeating character is ",i)
            break
        d+=i
