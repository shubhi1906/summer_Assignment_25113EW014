s=input("enter a string")
g=input("enter a string with which you want to check")
if len(s)!=len(g):
    print("rotation not possible")
else:
    f=0
    for i in range(len(s)):
        s=s[1:]+s[0]
        if s==g:
            f=1

    if f==0:
        print("rotation not successfull")
    else:
        print("rotation checked")
            
