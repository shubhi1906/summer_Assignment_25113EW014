arr = []

while True:
    print("\nMENU DRIVEN ARRAY OPERATIONS")
    print("1.Insert element")
    print("2.Delete element")
    print("3.Display array")
    print("4.Search element")
    print("5.Exit")

    choice=int(input("Enter your choice: "))

    if choice==1:
        n=int(input("Enter element to insert: "))
        arr.append(n)
        print("Element inserted")

    elif choice==2:
        n=int(input("Enter element to delete: "))
        if n in arr:
            arr.remove(n)
            print("Element deleted")
        else:
            print("Element not found")

    elif choice==3:
        print("Array =",arr)

    elif choice==4:
        n=int(input("Enter element to search: "))
        if n in arr:
            print("Element found at index", arr.index(n))
        else:
            print("Element not found")

    elif choice==5:
        print("thankyou!")
        break
    else:
        print("Invalid choice")
