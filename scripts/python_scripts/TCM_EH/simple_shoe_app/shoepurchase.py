#Created for TCM Academy Practical Ethical Hacker course
#!/bin/python3

from shoes import shoes

low = shoes("And 1s", 30)
medium = shoes("Air Force 1s", 120)
high = shoes("Off Whites", 400)

try:
	shoe_budget = float(input("What is your shoe budget? "))
	
except ValueError:
	exit('Please enter a number')
	
for shoes in [high, medium, low]:
	shoes.buy(shoe_budget)
