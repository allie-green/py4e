"""
3.2
Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program.
"""
error = "Error, please enter numeric input"

# check users input
s_hours = input("Hours: ")
try:
    hours = float(s_hours)
except:
    print(error)
    quit()

s_rate = input("Rate per hour: ")
try:
    rate = float(s_rate)
except:
    print(error)
    quit()

# calculate pay
if hours <= 40:
    pay_regular = hours * rate
    print(pay_regular)

# calculate pay with extra hours
elif hours > 40:
    aboveHours = hours - 40
    aboveRate = rate * 1.5

    pay_extra = 40 * rate + (aboveHours * aboveRate)
    print(pay_extra)
