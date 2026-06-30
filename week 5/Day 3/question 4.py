inventory = {}

while True:
    print("\nINVENTORY MANAGEMENT SYSTEM")
    print("1. Add Item")
    print("2. Update Item Quantity")
    print("3. Delete Item")
    print("4. Display Inventory")
    print("5. Search Item")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter item name: ")
        qty = int(input("Enter quantity: "))
        inventory[item] = qty
        print("Item added")

    elif choice == 2:
        item = input("Enter item name to update: ")
        if item in inventory:
            qty = int(input("Enter new quantity: "))
            inventory[item]=qty
            print("Item updated")
        else:
            print("Item not found")

    elif choice==3:
        item=input("Enter item name to delete: ")
        if item in inventory:
            del inventory[item]
            print("Item deleted")
        else:
            print("Item not found")

    elif choice==4:
        print("Inventory:")
        for item, qty in inventory.items():
            print(item, ":", qty)

    elif choice==5:
        i=input("Enter item name to search: ")
        if i in inventory:
            print(i,"quantity=",inventory[i])
        else:
            print("Item not found")
    elif choice==6:
        print("thankyou!")
        break
    else:
        print("Invalid choice")
