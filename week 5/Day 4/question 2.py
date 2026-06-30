book=[]
while True:
    print('''LIBRARY MANAGEMENT SYSTEM
          \n choose 1 to display all books
          \n choose 2 to add book
          \n choose 3 to search book
          \n choose 4 to update book
          \n choose 5 to delete book
          \n choose 6 to exit''')
    choice=int(input("enter your choice"))
    if choice==1:
        if len(book)==0:
            print("no record found")
        else:
            print("all records:")
            for i in book:
                print("book id:"  ,i[0])
                print("book name:"     ,i[1])
                print("author:",i[2])
                print("genre:",i[3])
                print("no. of copies:",i[4])
    elif choice==2:
        r=int(input("enter book id:"))
        n=input("enter book's name:")
        a=input("enter author name:")
        c=input("enter genre:")
        b=int(input("enter no. of copies:"))
        s=[r,n,a,c,b]
        book.append(s)

        print("record added")
    elif choice==3:
        f=int(input("enter id of the book that you want to search"))
        found = False
        for i in book:
            if i[0] == f:
                print("Record Found")
                print("book id:",i[0])
                print("book Name:",i[1])
                print("author:",i[2])
                print("genre:",i[3])
                print("copies:",i[4])
                found = True
                break

        if found == False:
            print("book not found.")

    elif choice==4:
        u=int(input("enter book id to update data of the book"))
        found = False
        for i in book:
            if i[0]==u:
                i[1]=input("Enter new name: ")
                i[2]=input("Enter new author: ")
                i[3]=input("Enter new genre: ")
                i[4]=int(input("Enter new no. of copies: "))
                found = True
                break

        if found == False:
            print("book not found.")

    elif choice == 5:
        d=int(input("Enter book id to delete: "))
        found=False

        for i in book:
            if i[0]==d:
                book.remove(i)
                print("Record deleted successfully.")
                found=True
                break

        if found==False:
            print("book not found.")
    elif choice==6:
        print("exit successful")
        break
    else:
        print("invalid choice")


