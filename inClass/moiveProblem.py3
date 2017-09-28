def total_profit(attendees):
	"""(number) -> float
	this function calculates the total profit for a movie theater
	given a number of people in attendence the argument attendees

	number of people must be greater than zero
	>>> total_profit(5)
	2.5
	>>> total_profit(2)
	-11.0
	>>> total_profit(100)
	430.0
	"""
	return ((attendees*5)-(attendees*0.5))-20
	
print (total_profit(5))
