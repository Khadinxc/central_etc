#Created for during Certificate 4 in Cybersecurity
print("Hello, welcome to the temperature converter! ")
temp = (input("What type of temperature would you like to convert?.. F for fahrenheit C for celsius!..:"))
if temp == "F" or "f":
    input_string = input('Enter Fahrenheit values for conversion to celsius separated by space ')
    print("\n")
    my_list = input_string.split()
    print('You entered:', my_list)
    print("Those temperatures in Celsius are...: ", [(int(x) - 32) * 5 / 9 for x in my_list])


elif temp == "C" or "c":
    input_string = input('Enter Celsius values for conversion to Fahrenheit separated by space ')
    print("\n")
    my_list = input_string.split()
    print('You entered:', my_list)
    print("Those temperatures in Fahrenheit are...: ", [(int(x) * 9 / 5) + 32 for x in my_list])
