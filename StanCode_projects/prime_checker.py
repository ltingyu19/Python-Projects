"""
File: prime_checker.py
Name: 劉庭宇
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

EXIT = -100

def main():
	"""
	---Algo---
	1. Print "Welcome to the prime checker!
	2. determine if the number is a prime number
	3. show message

	"""
	print("Welcome to the prime checker!")

	# Ask for initial input
	n = int(input("n: "))

	# Since while loop is only option and while True is not allowed, at n>1 condition, test if number is divisible for 2~9
	# If divisible, then it is not a prime number, if not, it is

	while n>1:
		if n%2 == 0:
			if n == 2: # Since 2,3,5,7 are prime numbers, extra if statement is needed to ensure program knows that they are prime numbers
				print(str(n) +" is a prime number.")
				n = int(input("n: ")) # Additional re-assign varialbe command to ensure infinite loop does not happen
			else:
				print(str(n) +" is not a prime number.")
				n = int(input("n: "))

		elif n%3 == 0:
			if n == 3:
				print(str(n) +" is a prime number.")
				n = int(input("n: "))
			else:
				print(str(n) +" is not a prime number.")
				n = int(input("n: "))


		elif n%4 == 0:
			print(str(n) +" is not a prime number.")
			n = int(input("n: "))

		elif n%5 == 0:
			if n == 5:
				print(str(n) +" is a prime number.")
				n = int(input("n: "))
			else:
				print(str(n) +" is not a prime number.")
				n = int(input("n: "))

		elif n%6 == 0:
			print(str(n) +" is not a prime number.")
			n = int(input("n: "))


		elif n%7 == 0:
			if n == 7:
				print(str(n) +" is a prime number.")
				n = int(input("n: "))
			else:
				print(str(n) +" is not a prime number.")
				n = int(input("n: "))


		elif n%8 == 0:
			print(str(n) +" is not a prime number.")
			n = int(input("n: "))
		elif n%9 == 0:
			print(str(n) +" is not a prime number.")
			n = int(input("n: "))

		else:
			# any other number that is NOT divisible with above criteria is a prime number
			print(str(n)+" is a prime number.")
			n = int(input("n: "))


	# Exit command, calling sentinel value
	if n==EXIT:
		print("Have a good one!")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
