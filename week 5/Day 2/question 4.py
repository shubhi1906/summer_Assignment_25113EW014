contact=[]
while True:
    print('''CONTACT MANAGEMENT SYSTEM
          \n choose 1 to display all contacts
          \n choose 2 to add a contact
          \n choose 3 to search a contact
          \n choose 4 to update a contact
          \n choose 5 to remove a contact
          \n choose 6 to exit''')
    choice=int(input("enter your choice"))
    if choice==1:
        if len(contact)==0:
            print("no contacts")
        else:
            for i in contact:
                print("contact no.",i[0])
                print("name:",i[1])
                print("email:",i[2])
                print("address",i[3])
    elif choice==2:
        p=int(input("enter contact number:"))
        n=input("enter name:")
        e=input("enter email address:")
        a=input("enter address:")
        print("contact added")
        c=[p,n,e,a]
        contact.append(c)
    elif choice==3:
        s=int(input("enter contact number that you want to search:"))
        found=False
        for i in contact:
            if i[0]==s:
                print("contact found")
                print("contact no.",i[0])
                print("name:",i[1])
                print("email:",i[2])
                print("address:",i[3])
                found=True
                break
        if found==False:
            print("contact not found")
    elif choice==4:
        u=int(input("enter contact no. that you want to update:"))
        found=False
        for i in contact:
            if i[0]==u:
                i[1]=input("enter new name:")
                i[2]=input("enter new email address:")
                i[3]=input("enter new address:")
                print("contact updated")
                found=True
                break
        if found==False:
            print("contact not found")
    elif choice==5:
        d=int(input("enter the contact no. that you want to delete:"))
        for i in contact:
            if i[0]==d:
                contact.remove(i)
                print("contact removed")
    elif choice==6:
        print("thankyou!")
        break
    else:
        print("invalid choice")
