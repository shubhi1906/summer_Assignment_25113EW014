pin=1234
bal=5000
p=int(input("enter pin"))
if p==pin:
    while True:
        print(''' enter 1 for balance check
            \n enter 2 for money deposit
            \n enter 3 for withdrawl
            \n enter 4 for exit''')

        ch=int(input("enter choice"))
        if ch==1:
            print("balance=",bal)
        elif ch==2:
            amt=int(input("enter the amount you want to deposit"))
            bal+=amt
            print("deposit successful")
        elif ch==3:
            wdr=int(input("enter amount you want to withdrawl"))
            if wdr>bal:
                print("insufficient amount")
            else:
                bal-=wdr
        elif ch==4:
            print("thankyou!")
            break
        else:
            print("invalid choice!")
            
else:
    print("wrong pin")
