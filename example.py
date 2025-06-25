# this is a comment
# string
name=""
# int
age=20

# simple function to output formatted text
print(f"My name is {name} and I am {age} years old.")

# function with parameters.
# Prints out a formatted sentence containing the parameters
# Resuable and dynamic compared to line 8
def SamIAm(n, a):
    print(f"My name is {n} and I am {a} years old")

# Executes the function defined on line 13
SamIAm("Sam", 50)

# bool variable. Can be true or false
isAdult = age > 21

# if statement control flow
if isAdult:
    SamIAm("Daniel", 34)
else:
    SamIAm("DJ", 18)

# boolean for the following game
playTheGame = True

# continuous game loop
while playTheGame:
    # output
    print("What's your name?")
    # input
    myN = input()
    print("How old are you?")
    myA = input()
    # Use the input for an action
    SamIAm(myN, myA)
    print("Play again? (Y/N)")
    repeat = input()
    # determine whether game continues or ends
    if repeat.lower() == "Y".lower():
        continue
    else:
        print("bye!")
        break

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def iam(self):
        print(f"My name is {self.name} and I am {self.age} years old!")

DrJones = Person("Melanie", 30)
DrJones.iam()