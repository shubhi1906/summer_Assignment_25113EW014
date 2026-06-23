s=input("enter a string")
d=""
freq=[]
char=[]
for i in s:
       if i not in d:
           count=0
           for j in s:
               if i==j:
                   count+=1
           freq.append(count)
           char.append(i)
           d+=i     
m=max(freq)
for i in range(len(freq)):
    if freq[i]==m:
        print("maximum occuring element is ",char[i])
