"""
File: rocket.py
Name: 劉庭宇
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 3 Handout.

"""

# This constant determines rocket size.
SIZE = 5


def main():
    """
    ---Algo---
    1. Define Constant"SIZE"
    2. Define function "head" -- with value from SIZE, determining how many layers are needed
    3. Define function "belt"
    4. Define function "Upper body"
    5. Define function"Lower body"
    6. Use functions in "main()"
    """
    head()
    belt()
    upper_body()
    lower_body()
    belt()
    head()


def head():
    """
    This function draws the head of the rocket, the height of the head is defined by SIZE
    ---Algo---
    Print blank blocks ➜ left side head ➜ right side head

    """
    for i in range (SIZE):  # Height is defined by SIZE
        for j in range (SIZE-i):  # Print blank blocks
            print(" ", end="")
        for j in range (i+1):  # Print left side head
            print("/", end="")
        for j in range (i+1):  # Print right side head
            print("\\", end="")  # "\\" is required because back slash is a special string in python
        print("")


def belt():
    """
    This function draws the belt of the rocket, the length of the belt is defined by SIZE
    ---Algo---
    Print + ➜ Print middle ➜ Print +
    """
    print("+", end="")  # Print "+", since it should not be effected by SIZE, this command is out of for loop
    for i in range(SIZE*2):  # Print "=" with numbers defined by SIZE*2
        print("=", end="")
    print("+")  # Print "+", since it should not be effected by SIZE, this command is out of for loop, auto next line


def upper_body():
    """
    This function draws the upper body of the rocket, the height of the body is defined by SIZE
    ---Algo---
    Print | ➜ left dot ➜ Central /\➜ right dot ➜ print |
    """

    for i in range(SIZE): #Height is defined by SIZE
        for j in range(1): #Print | outer fuselage, since there will always be one fuselage symbol, range=1
            print("|", end="")
        for j in range(SIZE-(i+1)): #Print ".", as i starts from zero, extra i+1 is needed en ensure
                                    # only SIZE-1 numbers of dots at the top of the body
            print(".", end="")
        for j in range (i+1): #Print Central "/\" body
            print("/\\", end="")
        for j in range (SIZE-(i+1)): #Same as above
            print(".", end="")
        for j in range(1): #Same as above
            print("|")


def lower_body():
    """
    This function draws the lower body of the rocket, the height of the body is defined by SIZE
    ---Algo---
    Print | ➜ print dots ➜ Central \/ ➜ print dots ➜ print|
    """
    for i in range (SIZE): #Height is defined by SIZE
        for j in range(1): #Print | outer fuselage, since there will always be one fuselage symbol, range=1
            print("|", end="")
        for j in range(i): #Print ".", as i starts from 0~2 when set to 3, range = i
            print(".", end="")
        for j in range(SIZE-i): # Print central"\/" body
            print("\/", end="")
        for j in range (i): #Same as above
            print(".", end="")
        for j in range(1): #Same as above
            print("|")




# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
