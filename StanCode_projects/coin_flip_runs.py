"""
File: coin_flip_runs.py
Name: 劉庭宇
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	---Algo---
	1. get input for how many runs
	2. get random and define
	3. continuous loop until terminate
	"""

	# Print initial message and request number of runs, define necessary variables
	print("Let's flip a coin!")
	runs = int(input("Number of runs: "))
	rolls = ""
	can_add = True
	current_runs = 0

	# Initial roll for later determination
	roll_num1 = r.randint(0,1)
	if roll_num1 == 0:
		rolls += "H"
	else:
		rolls += "T"

	# If current runs != runs, continue with loop
	while current_runs != runs:
		roll_num2 = r.randint(0,1)

		# If initial roll == second run, use boolean from "can_add" to determine current run status
		if roll_num1 == roll_num2:
			if can_add:
				current_runs+=1
				# since has already add 1 run, set can_add to false to prevent erroneous calculation
				can_add=False
		# If initial roll != second run, reset/set can_add to true
		else:
			can_add=True

		# add string according to results
		if roll_num2 == 0:
			rolls += "H"
		else:
			rolls += "T"

		# set previous run to current run status as reset
		roll_num1 = roll_num2

	# print all messages
	print(str(rolls))







# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
