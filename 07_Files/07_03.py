"""
7.3
* Modify the program that prompts the user for the file name so that it prints a funny message when the user types in the exact file name “na na boo boo”. 
* The program should behave normally for all other files which exist and don’t exist.
* If the file exist return the num of lines that start with "Subject:"
"""
f_name = input("Enter the file name: ")
count = 0

if f_name == "na na boo boo":
	print(f"{f_name.upper()} TO YOU - You have been punk'd!")
	quit()

try:
	f_handle = open(f_name)
except:
	print(f"File cannot be opened: {f_name}")
	quit()

for line in f_handle:
	if line.startswith("Subject:"):
		count+= 1

print(f"There were {count} subject lines in {f_name}")