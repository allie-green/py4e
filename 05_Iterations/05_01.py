"""
5.1
* Write a program which repeatedly reads numbers until the user enters "done". 
* Once "done" is entered, print out the total, count, and average of the numbers.
* If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.
"""
total = 0
num_quantity = 0 # havin 3, 1, 4 and 5 would be num_quantity = 4

while True:
	user_input = input("Enter a number: ")

	if user_input == "done":
		break

	try:
		num = float(user_input)
	except:
		print("Invalid input")
		continue
	
	total = total + num
	num_quantity = num_quantity + 1

average = total / num_quantity	

print(total, num_quantity, average)
