#Created for TCM Academy Practical Ethical Hacker course
#!/bin/py

x = float(input("Give me a number: "))
o = input("Give me an operator: ")
y = float(input("Give me another number: "))

operators = ("+", "-", "/", "*")

if o == "+":
	print(x + y)
elif o == "-":
	print(x - y)
elif o == "/":
	print(x / y)		
elif o == "/":
	print(x / y)	
elif o == "*":
	print(x * y)	
elif o == "**" or o =="^":
	print(x ** y)	
else:
	print(o+" Isn't a valid operator please input either: "+str(operators))
	
