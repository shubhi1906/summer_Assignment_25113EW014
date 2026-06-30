bank=[]
while True:
    print('''BANK ACCOUNT SYSTEM
          \n choose 1 to display all accounts
          \n choose 2 to add account
          \n choose 3 to search account
          \n choose 4 to update account
          \n choose 5 to delete account
          \n choose 6 to deposit money"
          \n choose 7 to withdraw money"
          \n choose 8 to exit''')
    choice=int(input("enter your choice"))
    if choice==1:
        if len(bank)==0:
            print("no account found")
        else:
            print("all accounts:")
            for i in bank:
                print("account no.:",i[0])
                print("account holder name:",i[1])
                print("account type:",i[2])
                print("balance:",i[3])
    elif choice==2:
        n=int(input("enter account no.: "))
        h=input("enter account holder's name: ")
        t=input("enter account type: ")
        b=int(input("enter bank balance: "))
        a=[n,h,t,b]
        bank.append(a)
        print("account added ")
    elif choice==3:
        s=int(input("enter account no. that you want to search:"))
        found=False
        for i in bank:
            if i[0]==s:
                print("account found")
                print("account no.", i[0])
                print("account holder name:", i[1])
                print("account type:", i[2])
                print("balance:", i[3])
                found=True
                break
        if found==False:
            print("account not found")
    elif choice==4:
        u=int(input("enter no. of the account that you want to update: "))
        found=False
        for i in bank:
            if u==i[0]:
                i[1]=input("enter new account holder name: " )
                i[2]=input("enter new account type: ")
                i[3]=int(input("enter new balance: "))
                print("account updated")
                found=True
                break
        if found==False:
            print("account not found")
    elif choice==5:
        r=int(input("enter no. of account that you want to remove: "))
        found=False
        for i in bank:
            if r==i[0]:
                bank.remove(i)
                print("account removed")
                found=True
                break
        if found==False:
            print("account not found")
    elif choice==6:
        dp=int(input("enter account no.:"))
        found=False
        for i in bank:
            if i[0]==dp:
               amt=int(input("enter the amount that you want to deposit:"))
               i[3]+=amt
               print("deposit successful")
               print("updated balance:",i[3])
               found=True
               break
        if found==False:
            print("account not found")
    elif choice==7:
        wd=int(input("enter account no.:"))
        found=False
        for i in bank:
            if i[0]==wd:
               amt=int(input("enter the amount you want to withdraw:"))
               if amt<=i[3]:
                   i[3]-=amt
                   print("withdrawl successful")
                   print("remaining balance:",i[3])
               else:
                   print("insufficient balance")
            found=True
            break
        if found==False:
            print("account not found")
    elif choice==8:
        print("thankyou!")
        break
    else:
        print("invalid choice")
                  
        
