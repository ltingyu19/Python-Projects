"""
File: quadratic_solver.py
Name: 劉庭宇
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math

def main():
	"""
	---Algo---
	1. Print "stanCode Quadratic Solver!"
	2. Define a,b,c with user input
	3. classify roots according to discriminant value (if statement)
	4. depending on discriminant value, calculate root
	5. show message accordingly

	"""

	print("stanCode Quadratic Solver!")

	#  User input for a,b,c
	a = float(input("Enter a: "))
	b = float(input("Enter b: "))
	c = float(input("Enter c: "))

	#discriminant calculation
	dis = (b*b)-(4*a*c)

	#  y = math.sqrt(dis) needs to be in if statement of "if dis>0" to ensure error "math domain error" does not occur
	#  since sqrt(-1) does not exist

	# when dis>0, proceed to calculate root x1 & x2
	if dis > 0:
		y = math.sqrt(dis)
		x1 = ((-b)+(y))/(2*a)
		x2 = ((-b)-(y))/(2*a)
		(print("Two roots: "+ str(x1) + "," + str(x2)))

	# when dis==0, proceed to calculate root x1
	elif dis == 0:
		y = math.sqrt(dis)
		x1 = ((-b)+(y))/(2*a)
		(print("One root: "+ str(x1)))

	#  when dis==0, do not calculate sqrt since it does not exist and will cause an error,
	#  simply proceed to show "No real roots" message
	elif dis < 0:
		(print("No real roots"))




# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
