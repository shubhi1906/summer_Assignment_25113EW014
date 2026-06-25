n=int(input("enter no of element for array 1 "))
A=[0]*n
for i in range(0,n):
    x=int(input("enter elements in sorted manner="))
    A[i]=x

m=int(input("enter no of element for array 2 "))
B=[0]*m
for i in range(0,m):
    y=int(input("enter elements in sorted manner="))
    B[i]=y

C=[]
i=j=0
while i<len(A) and j<len(B):
    if A[i]<B[j]:
        C.append(A[i])
        i+=1
    else:
        C.append(B[j])
        j+=1
while i<len(A):
    C.append(A[i])
    i+=1
while j<len(B):
    C.append(B[j])
    j+=1
print("sorted array is =",C)
