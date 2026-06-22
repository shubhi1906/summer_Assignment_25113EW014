s= input("enter a sentence")
w=0
print(len(s))
for i in s:
    if "a"<=i<="z" or "A"<=i<="Z":
        w+=1
    elif i==" ":
        pass
    else:
        pass
print("number of words in the given sentence=",w)
