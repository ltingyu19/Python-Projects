"""
File: caesar.py
Name: 劉庭宇
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""

# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    ---Algo---
    1. Define ALPHABET and position
    2. ask for SECRET NUMBER
    3. ask for CIPHERED STRING
    4. run function
    5. print ans
    """
    sn = int(input('Secret Number: '))
    str = input("What's the ciphered string? ")
    decipher(str, sn)


def decipher(str, sn):
    """
    ---algo---
    1. create new_alphabet
    2. case-insensitive function(change everything into uppercase)
    3. translate string
    4. print ans

    :param str: str, string of the ciphered message
    :param sn: int, the secret number for decipher
    """

    new_str = ""  # new_str is the uppercase version of the original string message, this is to ensure case-insensitive
    new_alphabet = ""  # new_alphabet is to define the ciphered alphabet order
    ans = ""  # ans is the output of deciphered message

    # This part defines the "new_alphabet"
    crop = ALPHABET[26 - sn:]  # cropped part of the original ALPHABET is defined by secret number
    left_over = ALPHABET[:26 - sn]
    new_alphabet = crop + left_over

    # This part converts the original str(ciphered message) into uppercase format
    for i in range(len(str)):
        ch = str[i]
        if ch.islower():
            new_str += ch.upper()
        else:
            new_str += ch

    # This part deciphers the message inputted
    for i in range(len(new_str)):
        j = new_alphabet.find(new_str[i])  # define j as the variable for finding the index of the specific alphabet
        if j >= 0:  # If j returns value >= 0, meaning there IS a alphabet to be found, for "Punctuation marks" &
            # "SPACE" Therefore, only this part will determine if we need to check with ALPHABET with new index "j"
            ans = ans + ALPHABET[j]
        else:
            ans += new_str[i]  # If return value < 0, means its not an alphabet, just add it into the ans directly
    print("The deciphered string is: " + ans)


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
