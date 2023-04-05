# same output as ´11_finding_numbers.py´
# solved using list comprehension
# regular expressions
# and filehandle.read() method

import re
print(sum( [int(x) for x in re.findall('[0-9]+', open("regex_sum_1729292.txt").read())] ))