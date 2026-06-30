s = input("Enter a string: ")

while True:
    print("\nMENU DRIVEN STRING OPERATIONS")
    print("1.Find Length")
    print("2 Convert to Uppercase")
    print("3.Convert to Lowercase")
    print("4.Reverse String")
    print("5.Count Vowels")
    print("6.Exit")

    choice=int(input("Enter your choice: "))

    if choice==1:
        print("Length=",len(s))

    elif choice==2:
        print("Uppercase=",s.upper())

    elif choice==3:
        print("Lowercase=",s.lower())

    elif choice==4:
        print("Reverse =",s[::-1])

    elif choice==5:
        c=0
        for ch in s:
            if ch.lower() in "aeiou":
                c+=1
        print("Vowel count=",c)

    elif choice==6:
        print("thankyou")
        break

    else:
        print("Invalid choice")
