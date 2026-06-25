print("welcome to the quiz")
score=0

print("Q1. What is the capital of Ireland?")
ans=input("Enter answer: ")

if ans.lower()=="dublin":
    print("Correct!")
    score+=1
else:
    print("Wrong!")

print("Q2. How many days are there in a week?")
ans=input("Enter answer: ")

if ans=="7":
    print("Correct!")
    score+=1
else:
    print("Wrong!")

print("Q3. What is the currency of bangladesh called?")
ans=input("enter answer:")

if ans.lower()=="taka":
    print("correct!")
    score+=1
else:
    print("wrong!")

print("Your score is", score)
