"""
5.2 
* Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
* Once 'done' is entered, print out the largest and smallest of the numbers.
* If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
* Enter 7, 2, bob, 10, and 4 and match the output below.

Invalid input
Maximum is 10
Minimum is 2

"""
smallest = None
largest = None

while True:
	user_input = input("Enter number: ")

	if user_input == "done":
		break

	try:
		num = int(user_input)
	except:
		print("Invalid input")
		continue

	if largest is None or num > largest:
		largest = num
	elif smallest is None or num < smallest:
		smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)