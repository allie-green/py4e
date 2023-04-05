"""
7.2 Write a program to prompt for a file name, and then read through the file and look for lines of the form 'X-DSPAM-Confidence: 0.8475'

When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line. Count these lines and then compute the total of the spam confidence values from these lines. When you reach the end of the file, print out the average spam confidence.
"""
f_name = input("Enter a file name: ")
f_handle = open(f_name)

count= 0
total_float = 0

for line in f_handle:
	if line.startswith("X-DSPAM-Confidence: "):
		
		f_num = float(line[20:])
		total_float += f_num
		count +=1

average_spam = total_float / count

print("Average spam confidence:",average_spam)	
#mbox-short.txt