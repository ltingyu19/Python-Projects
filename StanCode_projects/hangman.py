"""
File: hangman.py
Name:劉庭宇
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""

import random

# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    ---Algo---
    1. Random word and constant N_TURNS are defined
    2. read how many alphabets are in the ans, show message
    3. find if alphabet inputted is in ans and record current guessing status
    4. return message (correct, wrong, illegal format)
    5. record how many chances are left
    6. return win or lose message
    """
    # Basic inputs definition
    word = random_word()
    print(word)
    op = N_TURNS  # Import constant value to define how many chances the player has left

    # Define ans_old == "_____"
    ans_old = ""
    print("The word looks like: ", end="")
    for i in range(len(word)):
        ans_old += "-"
    print(ans_old)
    print("You have " + str(op) + " wrong guesses left.")

    # While opportunities > 0 proceed function
    while op > 0:
        input_ch = input("Your guess: ")
        input_ch_new = ""

        # case-insensitive (turn all to uppercase)
        if len(input_ch) == 1:
            if input_ch.isalpha():

                input_ch_new = input_ch.upper()

                # find word and define variable j
                j = word.find(input_ch_new)

                # If j>=0, in word, if statement initiates as when answer is correct
                if j >= 0:
                    print("You are correct!")
                    ans_new = (ans_determine(word, input_ch_new, ans_old))
                    print(ans_new)
                    ans_old = ans_new

                    if ans_new == word:
                        print("You win!!")
                        print("The answer is: " + word)
                        break

                # If j<0, not in word , if statement initiates as when answer is incorrect
                if j < 0:

                    op -= 1
                    if op == 0:
                        print("There is no " + input_ch_new + "'s" + " in the word.")
                        break
                    if op >= 1:
                        print("There is no " + input_ch_new + "'s" + " in the word.")

                        ans_new = (ans_determine(word, input_ch_new, ans_old))

                        ans_old = ans_new
                        print("The word looks like: " + ans_new)
                        print("You have " + str(op) + " wrong guesses left.")
            else:
                print("Illegal format")  # for if input is digit, show illegal format
        else:
            print("Illegal format")  # for any input that is more than index=1, show illegal format

    if op == 0:
        print("You are completely hung :(")
        print("The answer is: " + word)


# used to determine and show the current status of guessing words
def ans_determine(word, input_ch_new, ans_old):
    """
    ---algo---
    1. define new str (ans_new)
    2. define 3 conditions to edit the new str
    3. return value to main()

    :param word: str, the answer
    :param input_ch_new: str, the character inputted by user, re-modified to uppercase format
    :param ans_old: str, the current status of guessing words, ex. "---" ➜ "-A-" ➜  "CA-"
    """
    ans_new = ""

    for i in range(len(word)):

        if input_ch_new == word[i]:  # if user input == certain character in word, add character to new str
            ans_new += input_ch_new

        elif ans_old[i].isalpha():  # if ans_old("Last version of ans_new) contains character, keep character in str
            ans_new += ans_old[i]

        else:  # other conditions: just add "-" to str
            ans_new += "-"

    return ans_new


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
