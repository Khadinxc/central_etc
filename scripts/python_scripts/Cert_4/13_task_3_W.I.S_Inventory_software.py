#Created for during Certificate 4 in Cybersecurity
#Date: 16/10/21
#Version: 1.0
#W.I.S inventory system


#To use this program only input what is asked by the app, any unknown commands may terminate the code and require a re-run




import fileinput


def menu_display():
    print('+-=============================-+')
    print('= W.I.S (Widget inventory System) =')
    print('+-=============================-+')
    print('(1) Add New User')
    print('(2) Display all users')
    print('(3) Salary Calculator')
    print('(4) Gadget Cost Calculator')
    print('(5) Add new item to Inventory')
    print('(6) Update Inventory')
    print('(7) Remove item from Inventory')
    print('(8) Print Inventory Report')
    print('(99) Quit')
    choice = int(input("Enter choice: "))
    menu_selection(choice)


def menu_selection(choice):
    if choice == 1:
        add_new_user()
    elif choice == 2:
        display_users()
    elif choice == 3:
        salary_calculator()
    elif choice == 4:
        gadget_calculator()
    elif choice == 5:
        add_inventory()
    elif choice == 6:
        update_inventory()
    elif choice == 7:
        delete_inventory_item()
    elif choice == 8:
        print_inventory()
    elif choice == 99:
        exit()


def add_new_user():
    all_users = open('all_users.txt', 'a')
    print("Adding Inventory")
    print("================")
    user_name = input("Enter your name: ")
    user_number = input("Enter your phone number: ")
    user_designation = input("Enter your designation: ")
    all_users.write(user_name + '\n')
    all_users.write(user_number + '\n')
    all_users.write(user_designation + '\n')
    all_users.close()
    choice = int(input('Enter 98 to continue or 99 to exit: '))
    if choice == 98:
        menu_display()
    else:
        exit()


def display_users():
    global user_numbers, user_desig
    all_users = open('all_users.txt', 'r')
    print('All Current Users')
    print('<----------------->')
    content = all_users.readline()
    print([line.strip() for line in open("all_users.txt")])
    all_users.close()

    choice = int(input('Enter 98 to continue or 99 to exit: '))
    if choice == 98:
        menu_display()
    else:
        exit()


def salary_calculator():
    print("Hello welcome to the W.I.S built-in salary calculator, all information is not saved in this system.")
    hour_wage = input("Please enter your hourly wage.: ")
    print("Your salary per month is.. :", ((int(hour_wage) * 40 * 52) / 12), '!\n')
    print("Would you like to run the program again?\n")
    choice = input("y/n: ")

    if choice == "y":
        salary_calculator()

    elif choice == "n":
        print("Returning to menu...")
        menu_display()


def gadget_calculator():
    print("Hello Welcome to the W.I.S built-in gadget cost calculator.")
    gadget_price = input("Please enter the price of the gadget.: ")
    gadget_amount = input("Please enter the amount of gadgets you would like.: ")
    print("The cost of all these gadgets are.. :", (int(gadget_price)) * (int(gadget_amount)), '!\n')
    print("Would you like to run the program again?\n")
    choice = input("y/n: ")

    if choice == "y":
        gadget_calculator()

    elif choice == "n":
        print("Returning to menu...")
        menu_display()


def add_inventory():
    gadget_file = open('gadget_inventory.txt', 'a+')
    print("Adding Gadgets")
    print("+-================-+")
    item_description = input("Enter the name of the item: ")
    item_quantity = input("Enter the quantity of the item: ")
    gadget_file.write(item_description + '\n')
    gadget_file.write(item_quantity + '\n')
    gadget_file.close()
    choice = int(input('Enter 98 to continue or 99 to exit: '))
    if choice == 98:
        menu_display()
    elif choice == 99:
        exit()


def update_inventory():
    print("Updating Gadget Inventory")
    print("+-==================-+")
    item_description = input('Enter the item to update: ')
    item_quantity = int(input("Enter the updated quantity. Enter - for less: "))

    with open('gadget_inventory.txt', 'r') as f:
        filedata = f.readlines()

    replace = ""
    line_number = 0
    count = 0
    f = open('gadget_inventory.txt', 'r')
    file = f.read().split('\n')
    for i, line in enumerate(file):
        if item_description in line:
            for b in file[i + 1:i + 2]:
                value = int(b)
                change = value + item_quantity
                replace = b.replace(b, str(change))
                line_number = count
            count = i + 1
    f.close()

    filedata[count] = replace + '\n'

    with open('gadget_inventory.txt', 'w') as f:
        for line in filedata:
            f.write(line)

    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
        menu_display()
    else:
        exit()


def delete_inventory_item():
    print("Removing Inventory")
    print("+-==================-+")
    item_description = input("Enter the item name to remove from inventory: ")

    file = fileinput.input('gadget_inventory.txt', inplace=True)

    for line in file:
        if item_description in line:
            for i in range(1):
                next(file, None)
        else:
            print(line.strip('\n'), end='\n')
    choice = int(input('Enter 98 to continue or 99 to exit: '))
    if choice == 98:
        menu_display()
    else:
        exit()


def print_inventory():
    gadget_inventory = open('gadget_inventory.txt', 'r')
    item_description = gadget_inventory.readline()
    print('Current Gadgets')
    print('-----------------')
    while item_description != '':
        item_quantity = gadget_inventory.readline()
        item_description = item_description.rstrip('\n')
        item_quantity = item_quantity.rstrip('\n')
        print('Item:     ', item_description)
        print('Quantity: ', item_quantity)
        item_description = gadget_inventory.readline()
    gadget_inventory.close()
    print('-----------------')

    choice = int(input('Enter 98 to continue or 99 to exit: '))
    if choice == 98:
        menu_display()
    else:
        exit()


def detail_input():
            all_users = open('all_users.txt', 'a+')
            print("Let's get your details!")
            print("================")
            user_name = input("Enter your name: ")
            user_number = input("Enter your phone number: ")
            user_designation = input("Enter your designation: ")
            all_users.write(user_name + '\n')
            all_users.write(user_number + '\n')
            all_users.write(user_designation + '\n')
            all_users.close()
            menu_display()


print('Hello welcome to W.I.S (Widget inventory System)')


detail_input()
