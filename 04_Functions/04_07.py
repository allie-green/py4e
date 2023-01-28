"""
4.7 Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.
"""
def computegrade(score):

	#check that input is a numeric value
	try:
		score = float(s_score)
	except:
		return("Bad score")

	if score > 1.00:
		return("Bad score")
	elif score < 0.00:
		return("Bad score")

	elif score >= 0.9:
		return("A")
	elif score >= 0.8:
		return("B")
	elif score >= 0.7:
		return("C")
	elif score >= 0.6:
		return("D")
	elif score < 0.6:
		return("F")

s_score = input("Score? ")
print(computegrade(s_score))


