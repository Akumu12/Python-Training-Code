#Lab 2

#Part 1

'''
age = int(input("What is your age?"))

if age > 18:
    print("You are in Category A")
elif age >= 16:
    print ("You are in Category B")
elif age < 16:
    print("You are in Category C")
'''

#Part2 - Calculator

'''
print (" This calculator has operations Add, Subtract, Multiply, Divide and Square")

Number1 = float(input("What is your first number? "))
Number2 = float(input("What is your second number? "))

choice = input("What operation would you like to perform? ")

choice = choice.upper()

if choice == "ADD":
    print("Your answer is ",  (Number1 + Number2))
if choice == "SUBTRACT":
    print("Your answer is ",  (Number1 - Number2))
if choice == "MULTIPLY":
    print("Your answer is ",  (Number1 * Number2))
if choice == "DIVIDE":
    print("Your answer is ",  (Number1 / Number2))
if choice == "SQUARE":
    print("Number 1 squared is: ", (Number1 * Number1)) 
    print("Number 2 squared is" , (Number2 * Number2))
'''
#Part 3- Exam Grades
'''
Level = int(input("Is your current level 1 or 2? "))

valid = False
while valid == False:
    grade = int(input("What is your score? "))
    if grade > 100 or grade < 1:
        valid = False
        print("Please enter a score between 1 and 100")
    else:
        valid = True

if valid == False:
    print("Please enter a score between 1 and 100")

if valid == True and Level == 1:
    if grade < 50:
        print( "You have Failed")
    elif grade >= 50:
        print( "You have achieved a pass")
    elif grade >= 61:
        print( "You have achieved a merit")
    elif grade >= 71:
        print( "You have achieved a distinction")

elif valid == True and Level == 2:
    if grade < 40:
        print( "You have Failed")
    elif grade >= 40:
        print( "You have achieved a pass")
    elif grade >= 51:
        print( "You have achieved a merit")
    elif grade >= 66:
        print( "You have achieved a distinction")
'''
#Task 4 - Pythagoras

print("1 is A, 2 is B and 3 is C")
MissingSide = int(input("Please enter the number of the side you are trying to find?"))


if MissingSide == 1:
    B = int(input("What is the length of the first side? "))
    C = int(input("What is the length of the second side? "))
    A = (B**2) + (C**2)
    A = (A**0.5)
    print("The value of A is: ", A)
elif MissingSide == 2:
    A = int(input("What is the length of the first side? "))
    C = int(input("What is the length of the second side? "))
    B = (A**2) + (C**2)
    B = (B**0.5)
    print("The value of B is: ", B)
elif MissingSide == 3:
    A = int(input("What is the length of the first side? "))
    B = int(input("What is the length of the second side? "))
    C = (A**2) + (B**2)
    C = (C**0.5)
    print("The value of C is: ", C)
