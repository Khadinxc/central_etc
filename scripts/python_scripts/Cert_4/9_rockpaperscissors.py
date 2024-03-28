#Created for during Certificate 4 in Cybersecurity
###Belongs on Programmer horror###
#Date: 9/1/2021
#Version: 1.0
#
#Rock Paper Scissors game
#Two players




print("Welcome to Rock, Paper, Scissors!")
print("Let's begin...")
name1=input("Player 1: What's your name?")
name2=input("Player 2: What's your name?")


print("Hello", name1 ,"and", name2)
print(name2, "Close your eyes!")

choice1=input(name1+": Enter 'r' for rock, 'p' for paper, and 's' for scissors:")
print("Great choice! Now - cover your answer and ask", name2,"to choose.")
choice2=input(name2+": Enter 'r' for rock, 'p' for paper, and 's' for scissors:")

if(choice1=="r") and (choice2=="p"):
    print(name2,"is the winner!")
    print ("Thanks for playing Rock, Paper, Scissors")
elif (choice1=="p") and (choice2=="p"):
    print ("You both chose the same!")
    print ("Thanks for playing Rock, Paper, Scissors")
elif (choice1=="s") and (choice2=="p"):
    print (name1, "is the winner!")
    print ("Thanks for playing Rock, Paper, Scissors")
elif (choice1=="p") and (choice2=="r"):
    print (name2, "is the winner!")
    print ("Thanks for playing Rock, Paper, Scissors")
elif (choice1=="r") and (choice2=="r"):
    print ("You both chose the same!")
    print ("Thanks for playing Rock, Paper, Scissors")
elif (choice1=="s") and (choice2=="r"):
    print (name2, "is the winner!")
    print ("Thanks for playing Rock, Paper, Scissors")
elif (choice1=="p") and (choice2=="s"):
    print (name2, "is the winner!")
    print ("Thanks for playing Rock, Paper, Scissors")
elif (choice1=="r") and (choice2=="s"):
    print (name1, "is the winner!")
    print ("Thanks for playing Rock, Paper, Scissors")
elif (choice1=="s") and (choice2=="s"):
    print ("You both chose the same!")
    print ("Thanks for playing Rock, Paper, Scissors")
