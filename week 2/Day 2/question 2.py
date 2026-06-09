for i in range(0,5):
    num=1
    for j in range(0,5):
        if j>=i:
            print(num,end="")
            num+=1
        else:
            print("",end="")
    print()
