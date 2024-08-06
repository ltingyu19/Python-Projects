"""
File: class_reviews.py
Name: 劉庭宇
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""

EXIT = "-1"


def main():
    """
    ---Algo---
    1. Ask user input (class)
    2. Ask for score score
    3. repeat above until exit code
    4. after exit code, calculate score and show

    """
    # Ask for initial input of class for later determination
    clas = input("Which class? ")
    count101 = 0
    count001 = 0

    # If clas == EXIT, then terminate and show message
    if clas == EXIT:
        print("No class scores were entered")

    # When initial clas is SC101, select programming course for 101
    elif clas[2] == "1":
        score101 = int(input("Score: "))
        max101 = score101
        min101 = score101
        avg101 = score101
        count101 += 1

        # 001 initial condition needs to be here so later can be calculated
        max001 = 0
        min001 = 0
        avg001 = 0

        # Start while True loop to calculate SC001 & SC101
        while True:
            clas = input("Which class? ")

            if clas == EXIT:
                break

            # If clas is SC101 Case
            elif clas[2] == "1":
                score101 = int(input("Score: "))

                if score101 > max101:
                    max101 = score101
                elif score101 < min101:
                    min101 = score101

                count101 += 1

                if count101 == 1:
                    min101 = score101

                avg101 = avg101 + score101

            # If clas is SC001 Case
            elif clas[2] == "0":
                score001 = int(input("Score: "))
                if score001 > max001:
                    max001 = score001
                elif score001 < min001:
                    min001 = score001

                count001 += 1

                if count001 == 1:
                    min001 = score001

                avg001 = avg001 + score001

        # after termination show message (cannot be directly under def main, otherwise when initial input == EXIT,
        # all message below will be shown as well
        if avg001 < 1:
            print("=============SC001=============")
            print("No score for SC001")
        else:
            print("=============SC001=============")
            print("Max(001): " + str(max001))
            print("Min(001): " + str(min001))
            print("Avg(001): " + str(avg001 / count001))

        if avg101 < 1:
            print("=============SC101=============")
            print("No score for SC101")
        else:
            print("=============SC101=============")
            print("Max(101): " + str(max101))
            print("Min(101): " + str(min101))
            print("Avg(101): " + str(avg101 / count101))

    # When initial clas is SC001, select programming course for 101
    elif clas[2] == "0":
        score001 = int(input("Score: "))
        max001 = score001
        min001 = score001
        avg001 = score001
        count001 += 1

        # 101 initial condition needs to be here so later can be calculated
        max101 = 0
        min101 = 0
        avg101 = 0

        # Start while True loop to calculate SC001 & SC101
        while True:
            clas = input("Which class? ")

            if clas == EXIT:
                break

            # If clas is SC101 Case
            elif clas[2] == "1":
                score101 = int(input("Score: "))

                if score101 > max101:
                    max101 = score101
                elif score101 < min101:
                    min101 = score101

                count101 += 1

                if count101 == 1:
                    min101 = score101

                avg101 = avg101 + score101

            # If clas is SC001 Case
            elif clas[2] == "0":
                score001 = int(input("Score: "))
                if score001 > max001:
                    max001 = score001
                elif score001 < min001:
                    min001 = score001

                count001 += 1

                if count001 == 1:
                    min001 = score001

                avg001 = avg001 + score001

        # after termination show message (cannot be directly under def main, otherwise when initial input == EXIT,
        # all message below will be shown as well
        if avg001 < 1:
            print("=============SC001=============")
            print("No score for SC001")
        else:
            print("=============SC001=============")
            print("Max(001): " + str(max001))
            print("Min(001): " + str(min001))
            print("Avg(001): " + str(avg001 / count001))

        if avg101 < 1:
            print("=============SC101=============")
            print("No score for SC101")
        else:
            print("=============SC101=============")
            print("Max(101): " + str(max101))
            print("Min(101): " + str(min101))
            print("Avg(101): " + str(avg101 / count101))


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
