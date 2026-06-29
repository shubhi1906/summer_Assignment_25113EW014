employees=[]
while True:
    print('''EMPLOYEE RECORD MANAGEMENT SYSTEM
          \n choose 1 to display all details
          \n choose 2 to add employee
          \n choose 3 to search employee
          \n choose 4 to update employee's details
          \n choose 5 to delete employe's details
          \n choose 6 to exit''')
    choice=int(input("enter your choice"))
    if choice==1:
        if len(employees)==0:
            print("no record found")
        else:
            print("all records:")
            for i in employees:
                print("employee's id:"  ,i[0])
                print("employee's name:"     ,i[1])
                print("employee's age:",i[2])
                print("designation:",i[3])
                print("salary",i[4])
    elif choice==2:
        r=int(input("enter employee's id"))
        n=input("enter employee's name")
        a=int(input("enter employee's age"))
        c=input("enter employee's designation")
        b=int(input("enter salary"))
        s=[r,n,a,c,b]
        employees.append(s)

        print("record added")
    elif choice==3:
        f=int(input("enter id of the employee that you want to search"))
        found = False
        for i in employees:
            if i[0] == f:
                print("Record Found")
                print("Id:",i[0])
                print("Name:",i[1])
                print("Age:",i[2])
                print("designation:",i[3])
                print("salary:",i[4])
                found = True
                break

        if found == False:
            print("employee not found.")

    elif choice==4:
        u=int(input("enter ID to update data of the employee"))
        found = False
        for i in employees:
            if i[0]==u:
                i[1]=input("Enter new name: ")
                i[2]=int(input("Enter new age: "))
                i[3]=input("Enter new designation: ")
                i[4]=int(input("Enter new salary "))
                found = True
                break

        if found == False:
            print("Student not found.")

    elif choice == 5:
        d=int(input("Enter id to delete: "))
        found=False

        for i in employees:
            if i[0]==d:
                employees.remove(i)
                print("Record deleted successfully.")
                found=True
                break

        if found==False:
            print("employee not found.")
    elif choice==6:
        print("exit successful")
        break
    else:
        print("invalid choice")

