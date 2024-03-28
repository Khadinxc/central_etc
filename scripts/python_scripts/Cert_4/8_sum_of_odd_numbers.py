#Created for during Certificate 4 in Cybersecurity
#Date: 13/09/21
#Version: 1.0
#
# Python Program to Calculate Sum of Odd Numbers from min to max
 
minimum = int(input(" Please Enter the Minimum Value : "))
maximum = int(input(" Please Enter the Maximum Value : "))
Oddtotal = 0


for number in range(minimum, maximum+1):
    if(number % 2 != 0):
        print("{0}".format(number))
        Oddtotal = Oddtotal + number

print("The Sum of Odd Numbers from 1 to {0} = {1}".format(number, Oddtotal)) 

