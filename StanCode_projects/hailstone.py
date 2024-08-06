"""
File: hailstone.py
Name: 劉庭宇
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""

EXIT = 1

def main():
    """
    ---Algo---
    1. Print "This program computes Hailstone sequences."
    2. Define "number" with user input
    3. Determine if the "number" is odd or even ||| if entered 1, show 0 steps
    4. print out message and do mathematical calculations("//" are used instead of "/" to ensure "int" outcome instead of "float")
    4.1 (((SINCE DIVISION ARE ONLY USED WHEN NUMBERS ARE EVEN, THERE WILL BE NO NUMBERS BEHIND THE DECIMAL POINT, thus mathematical results are not effected)))
    5. repeat until 1 appears

    """


    print("This program computes Hailstone sequences.")
    print(" ") # To give a blank line and fit the assignments requirement

    # Ask for initial data input, determine boundary condition
    number = int(input("Enter a number: "))
    if number == EXIT:
        print("It took 0 steps to reach 1.")

    # If user input is valid, continue with program, set initial step value to 0
    else:
        steps = 0
        while True:

            # Determine if value is EVEN, if it is, divided by 2, steps+1, if value after math equals to zero, trigger break
            if number % 2 == 0:
                print(str(number)+" is even, so I take half: "+ str(number//2))
                number = number//2
                steps = steps+1

                if number == EXIT:
                    break
            # Determine if value is ODD, if it is, 3n+1, steps+1, if value after math equals to zero, trigger break
            elif number % 2 ==1:
                print(str(number)+" is odd, so I make 3n+1: "+ str((3*number)+1))
                number = 3*number+1
                steps = steps + 1

                if number == EXIT:
                    break

        # After break been triggered, show how many steps was used
        print("It took " +str(steps)+ " steps to reach 1.")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
