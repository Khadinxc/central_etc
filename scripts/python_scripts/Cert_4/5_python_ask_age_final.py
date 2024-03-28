#Created for during Certificate 4 in Cybersecurity
#Date: 30/08/21
#Version: 1.0
#
# Python3 code to  calculate age in years
from datetime import date

print(date.today().year)

birth_year = input("What is your birth year? ")
answer = input("Has your birthday happened already? ")

#now it will display the correct age with a birthday message
age = int(date.today().year) - int(birth_year)
age_2 = int(date.today().year) - int(birth_year) - 1
if answer == "yes":
    print("Your age is!:", age)
    print("I am sure that was a good day!")
elif answer == "no":
    print("Your age is!:", age_2)
    print("I hope you will have a good one!")
