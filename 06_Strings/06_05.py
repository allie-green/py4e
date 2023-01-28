"""
6.5
Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.
"""

string = 'X-DSPAM-Confidence:0.8475'

colon_position = string.find(":")

sliced_string = string[colon_position+1: ]

float_num = float(sliced_string)

print(float_num)

