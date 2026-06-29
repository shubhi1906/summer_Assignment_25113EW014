students = []

while True:
    print(''' MARKSHEET GENERATION SYSTEM)
    \n choose 1 to display all details
          \n choose 2 to add student
          \n choose 3 to search student
          \n choose 4 to update student
          \n choose 5 to delete student
          \n choose 6 to exit''')
    choice=int(input("Enter your choice: "))

    if choice==1:
        if len(students)==0:
            print("No records found.")
        else:
            for i in students:
                print("Roll No:",i[0])
                print("Name:",i[1])
                print("English:",i[2])
                print("Maths:",i[3])
                print("Science:",i[4])
                print("Total:",i[5])
                print("Percentage:",i[6], "%")
                print("Grade:",i[7])

    elif choice==2:
        r=int(input("Enter Roll Number: "))
        n=input("Enter Name: ")
        e=int(input("Enter English Marks: "))
        m=int(input("Enter Maths Marks: "))
        s=int(input("Enter Science Marks: "))

        total=e+m+s
        p=total/3

        if p>=90:
            grade="A+"
        elif p>=80:
            grade="A"
        elif p>=70:
            grade="B"
        elif p>=60:
            grade="C"
        elif p>=50:
            grade="D"
        else:
            grade="Fail"

        st=[r,n,e,m,s,total,p,grade]
        students.append(st)

        print("Record added successfully.")

    elif choice==3:
        sr=int(input("Enter Roll Number to search: "))
        found=False

        for i in students:
            if i[0]==sr:
                print("Roll No:",i[0])
                print("Name :",i[1])
                print("English:",i[2])
                print("Maths:",i[3])
                print("Science:",i[4])
                print("Total:",i[5])
                print("Percentage:",i[6], "%")
                print("Grade:",i[7])
                found = True
                break

        if found==False:
            print("Student not found.")

    elif choice==4:
        u=int(input("Enter Roll Number to update: "))
        found=False

        for i in students:
            if i[0]==u:
                i[1]=input("Enter New Name: ")
                i[2]=int(input("Enter English Marks: "))
                i[3]=int(input("Enter Maths Marks: "))
                i[4]=int(input("Enter Science Marks: "))

                i[5]=i[2]+i[3]+i[4]
                i[6]=i[5]/3

                if i[6]>=90:
                    i[7]="A+"
                elif i[6]>=80:
                    i[7]="A"
                elif i[6]>=70:
                    i[7]="B"
                elif i[6]>=60:
                    i[7]="C"
                elif i[6]>=50:
                    i[7]="D"
                else:
                    i[7]="Fail"

                print("Record updated successfully.")
                found=True
                break

        if found==False:
            print("Student not found.")

    elif choice==5:
        d=int(input("Enter Roll Number to delete: "))
        found=False

        for i in students:
            if i[0]==d:
                students.remove(i)
                print("Record deleted successfully.")
                found=True
                break

        if found==False:
            print("Student not found.")

    elif choice==6:
        print("Exit successful")
        break

    else:
        print("Invalid choice.")
