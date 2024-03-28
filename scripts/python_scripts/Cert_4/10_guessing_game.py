#Created for during Certificate 4 in Cybersecurity
#Date: 30/08/21
#Version: 1.0
#
#Guess the random number game
#One player vs. the computer

import random
random.randint(1,6)
number = random.randint(1,6)

x = " "

#Ask the user for their name and their guess
name = input("Hi what is your name?..:")
print("Hi!"+x+name,"welcome to the Guess the Number!")
print("Enter a number between 1 and 6")
guess = int(input("What is your guess?:"))

#Generate a random number and tell the user if they won or lost

if guess==number: 
 print("Congratulations, you got it right!")
 print("Thank you for playing Guess the Number!")
            
elif guess!=number:
 print("You lose - the number was:" , number)
 print("Thank you for playing Guess the Number!")
