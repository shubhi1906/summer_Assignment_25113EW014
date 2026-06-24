s=input("enter a sentence")
l=s.split()
m=l[0]
for i in l:
    if len(i)>len(m):
        m=i
print("the longest word in the sentence is ",m)
