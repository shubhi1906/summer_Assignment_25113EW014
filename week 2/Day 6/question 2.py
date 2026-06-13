n=int(input("enter number of elements in array"))
l=[]
for i in range(0,n):
    m=int(input("enter array elements"))
    l.append(m)

s=0
for i in l:
    s+=i
print("the sum is",s)
avg=s//n
print("the average is ",avg)
