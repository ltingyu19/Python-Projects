"""
File: complement.py
Name: 劉庭宇
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    ---Algo---
    1. define function:build_complement
    2. allow the commands in main() to show relative answers

    """
    #  Following command of using functions are defined by the question
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    """
    ---Algo---
    1. define parameters
    2. define relationships between (A,T,G,C), string manipulation
    2.1 Relationship: (A⮂ T, C⮂G)
    3. give correspondence answers

    :param a(dna): str
    :return: str
    """
    ans = ""  # Assign a empty string to edit
    if len(dna) > 1:  # if string length > 1, means there are inputs to be interpreted
        for i in range(len(dna)):  # using the length of the string, we can have a "for loop"
            ch = dna[i]  # define variable "ch" as string1, string2, string3, ...

            if ch == "A":  # when character encountered is A, add its counterpart T to string(ans)
                ans = ans + "T"
            elif ch == "T":  # when character encountered is T, add the its counterpart A to string(ans)
                ans = ans + "A"
            elif ch == "C":  # when character encountered is C, add its counterpart G to string(ans)
                ans = ans + "G"
            elif ch == "G":  # when character encountered is G, add its counterpart C to string(ans)
                ans = ans + "C"
        return ans  # Always return answering value to main(), regardless of how you use this value in main()
    else:
        return "DNA strand is missing."  # if string length < 1, meas there are NO inputs to be interpreted
        # Therefore, return with message, "DNA strand is missing."


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
