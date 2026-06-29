students=[]
while True:
    print('''STUDENT RECORD MANAGEMENT SYSTEM
          \n choose 1 to display all details
          \n choose 2 to add student
          \n choose 3 to search student
          \n choose 4 to update student
          \n choose 5 to delete student
          \n choose 6 to exit''')
    choice=int(input("enter your choice"))
    if choice==1:
        if len(students)==0:
            print("no record found")
        else:
            print("all records:")
            for i in students:
                print("roll no.:"  ,i[0])
                print("name:"     ,i[1])
                print("age:",i[2])
                print("course:",i[3])
                print("batch:",i[4])
    elif choice==2:
        r=int(input("enter student's roll no."))
        n=input("enter student's name")
        a=int(input("enter student's age"))
        c=input("enter student's course")
        b=int(input("enter ending year of the course"))
        s=[r,n,a,c,b]
        students.append(s)

        print("record added")
    elif choice==3:
        f=int(input("enter roll no. of the student that you want to search"))
        found = False
        for i in students:
            if i[0] == f:
                print("Record Found")
                print("Roll No:",i[0])
                print("Name:",i[1])
                print("Age:",i[2])
                print("Course:",i[3])
                print("batch:",i[4])
                found = True
                break

        if found == False:
            print("Student not found.")

    elif choice==4:
        u=int(input("enter roll no. to update data of the student"))
        found = False
        for i in students:
            if i[0]==u:
                i[1]=input("Enter new name: ")
                i[2]=int(input("Enter new age: "))
                i[3]=input("Enter new course: ")
                i[4]=int(input("Enter ending year of course: "))
                found = True
                break

        if found == False:
            print("Student not found.")

    elif choice == 5:
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
        print("exit successful")
        break
    else:
        print("invalid choice")

