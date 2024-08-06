"""
File: string_score.py
Name: 劉庭宇
------------------------------
This program calculates a score for a given string based on 
the types of characters it contains. It assigns points as follows: 
digits are worth 1 point, uppercase letters are worth 2 points, 
and lowercase letters are worth 3 points. The score() function 
goes through each character in the string, adds up the points 
according to its type, and then prints out the total score.
"""


def main():
    """
    ---Algo---
    1. call out score(str) function
    2. define score with function
    3. output results
    """
    score('1aB4rC')    # digit->1 ; upper->2; lower->3
    # 12
    score('aaaaA3')
    # 15


def score(str):
    """
    ---Algo---
    1. define parameters
    2. define relationships between (numbers=1, upper_case=2, lower_case=3), string manipulation
    3. give correspondence answers

    :param str: str, the string with numbers and alphabets
    :return: str, scores
    """

    ans = 0  # Define ans = 0 as an int.

    for i in range (len(str)):  # or can use "for i in str"

        ch = str[i]

        if ch.islower():  # When ch is lower case alphabet, add 3 to ans
            ans = ans + 3

        elif ch.isupper():  # When ch is upper case alphabet, add 2 to ans
            ans = ans + 2

        elif ch.isdigit():  # When ch is a number, add 1 to ans
            ans = ans + 1

    print (ans)  # Print out ans
    return ans  # Return ans value to main()




if __name__ == '__main__':
    main()