# 7.2 List version
f_name = input("Enter a file name: ")
f_handle = open(f_name)

count= 0
all_floats = list()

for line in f_handle:
	if line.startswith("X-DSPAM-Confidence: "):
		
		f_num = float(line[20:])
		all_floats.append(f_num)
		count +=1

average_spam = sum(all_floats) / count
print(count)
print("Average spam confidence:",average_spam)	
#mbox-short.txt