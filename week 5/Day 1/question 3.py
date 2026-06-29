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
                print("Employee ID :",i[0])
                print("Name :",i[1])
                print("Basic Salary:",i[2])
                print("HRA:",i[3])
                print("DA:",i[4])
                print("Gross Salary:",i[5])

    elif choice==2:
        emp_id=int(input("Enter Employee ID: "))
        name=input("Enter Employee Name: ")
        basic=float(input("Enter Basic Salary: "))
        hra=float(input("Enter HRA: "))
        da=float(input("Enter DA: "))

        gross=basic+hra+da

        e=[emp_id,name,basic,hra,da,gross]
        employees.append(e)

        print("Employee record added successfully.")

    elif choice==3:
        s=int(input("Enter Employee ID to search: "))
        found = False

        for i in employees:
            if i[0]==s:
                print("\nRecord Found")
                print("Employee ID :",i[0])
                print("Name :",i[1])
                print("Basic Salary:",i[2])
                print("HRA:",i[3])
                print("DA:",i[4])
                print("Gross Salary:",i[5])
                found=True
                break

        if found==False:
            print("Employee not found.")

    elif choice==4:
        u=int(input("Enter Employee ID to update: "))
        found=False

        for i in employees:
            if i[0]==u:
                i[1]=input("Enter New Name: ")
                i[2]=float(input("Enter New Basic Salary: "))
                i[3]=float(input("Enter New HRA: "))
                i[4]=float(input("Enter New DA: "))

                i[5]=i[2]+i[3]+i[4]

                print("Record updated successfully.")
                found = True
                break

        if found==False:
            print("Employee not found.")

    elif choice==5:
        d=int(input("Enter Employee ID to delete: "))
        found = False

        for i in employees:
            if i[0]==d:
                employees.remove(i)
                print("Record deleted successfully.")
                found=True
                break

        if found==False:
            print("Employee not found.")

    elif choice == 6:
        print("Exit successful")
        break

    else:
        print("Invalid choice.")
