"""
File: weather_master.py
Name: 劉庭宇
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100

def main():

	"""
    ---Algo---
    1. Print "stanCode "Weather Master 4.0"!
    2. ask for "temperature" with user input
    3. PK to find highest temp, lowest temp, average temp, days of low temp, and avg. temp
    4. with EXIT, show the above info
	"""
	print("stanCode \"Weather Master 4.0\"!")

	# Asking for first input on "temperature"
	temp = int(input("Next Temperature: (or -100 to quit)? "))

	# If user input = EXIT, print message
	if temp==EXIT:
		print("No temperature were entered")

	# If user input = valid, set current temp to max, low, accumulated temp, and plus one on recorded date
	else:
		maximum = temp
		lowest = temp
		accumulate_temp = temp
		days=1

		# To ensure the very first value are still accounted for cold warnings, extra if statement is used
		if temp < 16:
			cd_warning=1
		else:
			cd_warning=0


		# start while loop to ask user input new temp. data
		while True:
			temp = int(input("Next Temperature: (or -100 to quit)? "))

			if temp==EXIT:
				break
			# if use continuous if statement, but no indent, every if statement will run once,
			# causing numerical value to possibly addon to a erroneous result

			# Record hottest temperature, as well as "days" + "accumulated temperature value" + "possible cold warnings"
			# extra if statement of cold warnings are needed to ensure even when program enters this particular
			# elif statement, cd_warnings can still be recorded, otherwise when temp fits both "MAX&Cd_Warning"
			# criteria, normal cd_warning statement will not be triggered and thus leads to erroneous data.
			elif temp > maximum:
				maximum = temp
				days = days + 1
				accumulate_temp= accumulate_temp+temp
				if temp<16:
					cd_warning = cd_warning + 1

			# Record lowest temperature, as well as "days" + "accumulated temperature value" + "possible cold warnings"
			# extra if statement of cold warnings are needed to ensure even when program enters this particular
			# elif statement, cd_warnings can still be recorded, otherwise when temp fits both "MIN&Cd_Warning"
			# criteria, normal cd_warning statement will not be triggered and thus leads to erroneous data.
			elif temp < lowest:
				lowest = temp
				days = days + 1
				accumulate_temp = accumulate_temp + temp
				if temp<16:
					cd_warning = cd_warning + 1

			# Record cold warnings under normal circumstance + days + accumulated temperature
			elif temp < 16:
				cd_warning = cd_warning+1
				days = days + 1
				accumulate_temp = accumulate_temp + temp

			#  If the temperature inputed is not included in cold warning, hottest, coldest, then it will still
			#  be recorded with accumulated temperature and days
			else:
				days = days + 1
				accumulate_temp = accumulate_temp + temp

		print("Highest temperature = " +str(maximum))
		print("Lowest temperature = " +str(lowest))
		print("Average = " + str(accumulate_temp/days))
		print(str(cd_warning)+" cold day(s)")




# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
