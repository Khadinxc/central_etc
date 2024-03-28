#Created for TCM Academy Practical Ethical Hacker course
#!/bin/python3

#Print string
print("Hello, world!")
print('Hello, world!')
print("""This string runs
multiple lines!""") #Triple quote for multi-line
print("This string is " + "awesome") #We can also concatenate
print('\n') #Print new line
print('test that new line out')

print('\n') 
#MATH
print(50 + 50) #add
print(50 - 50) #subtract
print(50 * 50) #multiple
print(50 / 50) #divide
print(50 + 50 - 50 * 50 / 50) #PEMDAS
print(50 ** 2) #exponents
print(50 % 6) #modulo - takes what is left over
print(50 / 6) #division with remainder (or a float)
print(50 // 6) #no remainder

print('\n') 
#VARIABLES AND METHODS

quote = "All is fair in love and war."
print(quote)

print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title case
print(len(quote)) #Count characters in variable

name = "Kaiber" #string
age = 82 #integer
gpa = 3.9 #float - has a decimal

print(int(age)) #prints the integer held in the variable age
print(int(31.1)) #only prints what's on the left side of the decimal point, because of printing an int
print(int(30.9)) #will it round? no.

print("My name is " + name + " and I am " + str(age) + " years old.") #Concatenate different variables together.

age += 1 #Add an 1 to an integer within a variable
print(age)

birthday = 1 #declare a variable called birthday that has a value of 1
age += birthday #add two integers together.
print(age)

print('\n')
#FUNCTIONS

def who_am_i(): #this is a function without parameters
	name = "Kaiber" #local variable
	age = 901
	print("My name is " + name + " and I am " + str(age) + " years old.")
	

who_am_i()

def add_one_hundred(num):
	print(num + 100)
	
add_one_hundred(100)

def add(x,y):
	print(x + y)

add(7,7)

def multiple(x,y):
	return x * y #doesn't do the math but you're able to use the return to store a multiple into a variable

multiple(7,7) #you can store this in a variable
print(multiple(7,7)) #this actually prints the outcome of the multiplication

def square_root(x):
	print(x ** .5)

square_root(64)

def nl(): #new line
	print('\n')

nl()

#BOOLEAN EXPRESSIONS (TRUE OR FALSE)

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

bool5 = "True"
print(type(bool5))

nl()
#RELATIONAL AND BOOLEAN OPERATORS
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

test_and = (7 > 5) and (5 < 7) #True
test_and2 = (7 > 5) and (5 > 7) #False
test_or = (7 > 5) or (5 < 7) #True
test_or2 = (7 > 5) or (5 > 7) #True

test_not = not True #False

#CONDITIONAL STATEMENTS - if/else

def drink(money):
	if money >= 2:
		return "You've got yourself a drink"
	else:
		return "No drink for you"
print(drink(3))
print(drink(1))

def alcohol(age,money):
	if age>= 21 and money >= 5:
		return "Enjoy your drink"
	elif age>= 21 and money < 5:
		return "Get out you hobo"
	elif age < 21 and money >= 5:
		return "Get out come back when you're older"
	else: 
		return "Get out you're poor and too young"
print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,5))
print(alcohol(20,4))

nl()

#LISTS - HAVE BRACKETS []
movies = ["When Harry Met Sally", "The Hangover", "The Perks of Being a Wallflower", "The Exorcist"]
print(movies[1]) #Prints the second item in the list.
print(movies[0]) #Prints the first item in the list.
print(movies[1:3]) #return the first index number given right until the last number given, but not include the last number.
print(movies[1:])
print(movies[:1])
print(movies[-1]) # returns last item in list

print(len(movies))
movies.append("JAWS")
print(movies) #appends to the end of list.
movies.insert(2, "Hustle")
print(movies)

movies.pop() #removes the last item
print(movies)

movies.pop(0) #removes the first item
print(movies)

amber_movies = ['Just go with it','50 First Dates']
our_favourite_movies = movies + amber_movies
print(our_favourite_movies)

grades = [["Bob", 82], ["Alice",90], ["Jeff", 73]]
bobs_grade = grades[0][1]
print(bobs_grade)
grades[0][1] = 83
print(grades)

#TUPLES - LISTS THAT CANNOT BE CHANGED. They use () parenthesis rather than square brackets [] Tuples are Not mutable while lists are mutable
grades = ("a", "b", "c", "d", "f")
print(grades[1])
nl()
#LOOPING

#For loops - start to finish of an iterate
vegetables = ["cucumber", "spinach", "cabbage"]
for x in vegetables:
	print(x)
	
#192.168.1.1-254
#ip = 1..256
#for x in ip:
#	ping 192.168.1.x
	
#While loops - execute as long as True
i = 1

while i < 10:
	print(i)
	i += 1
nl()
#ADVANCED STRINGS

my_name = "kaiber"
print(my_name[0]) #first letter
print(my_name[-1]) #last letter - strings are imutable

sentence = "This is a sentence."
print(sentence[:4])
print(sentence.split()) #delimeter - default delimeter is a space.

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = "He said, 'give me all your money'"
print(quote)
quote = "He said, \"give me all your money\""
print(quote)

too_much_space = "                       hello                "
print(too_much_space)
print(too_much_space.strip())

print("A" in "Apple") #True
print("a" in "Apple") #False

letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) #improved 

movie = "The Hangover"
print("My favorite movie is {}.".format(movie))
print("My favorite movie is %s" % movie + ".")
print(f"My favorite movie is {movie}.")

nl()
#DICTIONARIES - key/value pairs {}

drinks = {"White Russian": 7, "Old Fashioned": 10, "Lemon Drop": 8} #drink is the key, price is the value.
print(drinks)

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teddy"], "HR": ["Jimmy Jr", "Mort"]}
print(employees)

employees['Legal'] = ["Mr. Frond"] #adds new key:value pair
print(employees)

employees.update({"Sales": ["Andie", "Ollie"]}) #adds new key:value pair
print(employees)

drinks['White Russian'] = 8
print(drinks)

print(drinks.get("White Russian"))
