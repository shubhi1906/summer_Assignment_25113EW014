n=int(input("enter no of element for array 1"))
l=[0]*n
for i in range(0,n):
    x=int(input("enter a sequence of numbers in sorted manner="))
    l[i]=x

s=int(input("enter the number you want to search"))
start=0
end=n-1
while start<=end:
    mid=(start+end)//2
    if l[mid]==s:
        print("element found at ", mid)
        break
    elif l[mid]<s:
        start=mid+1
    elif l[mid]>s:
        end=mid-1
else:
    print("element not found")
        
    
