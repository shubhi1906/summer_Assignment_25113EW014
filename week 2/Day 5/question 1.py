def palindrome(s):
        if s==s[::-1]:
            print("yes its palindrome")
        else:
            print("not a palindrome")


s=input("enter a string")
palindrome(s)
