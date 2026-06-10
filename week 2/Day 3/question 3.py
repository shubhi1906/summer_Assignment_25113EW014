for i in range(1,6):
    num=1
    for j in range(1,10):
        if (6-i)<=j<=(4+i):
            print(num,end="")
            if j<5:
                num+=1
            else:
                num-=1
        else:
            print(" ",end="")
    print()
