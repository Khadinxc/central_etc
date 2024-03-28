#Created for during Certificate 4 in Cybersecurity
# Date: 13/09/21
# Version: 1.0
# Basic grading application for a small school

Bob = {'name': 'bob', 'assignments': 80.0, 'presentation': 80.0, 'lab tasks': 60.0}
kaiber = {'name': 'kaiber', 'assignments': 90.0, 'presentation': 90.0, 'lab tasks': 90.0}
bob_list = [Bob['assignments'], Bob['presentation'], Bob['lab tasks'], ]
kaiber_list = [kaiber['assignments'], kaiber['presentation'], kaiber['lab tasks'], ]
bob_avg = sum(bob_list) / len(bob_list)
kaiber_avg = sum(kaiber_list) / len(kaiber_list)


def average():
    bob_scores = [Bob['assignments'], Bob['presentation'], Bob['lab tasks']]
    kaiber_scores = [kaiber['assignments'], kaiber['presentation'], kaiber['lab tasks']]

    numbers_lists = bob_scores + kaiber_scores
    all_students_avg = sum(numbers_lists) / len(numbers_lists)
    print("This is all the students average score across all subjects: ", all_students_avg)
    menu_display()


def get_average():
    bob_list = [Bob['assignments'], Bob['presentation'], Bob['lab tasks'], ]
    kaiber_list = [kaiber['assignments'], kaiber['presentation'], kaiber['lab tasks'], ]
    print("This function will show the average score of a specific student!")
    print("1. To see Bob")
    print("2. To see kaiber")
    choice1 = input("Who would you like to see?: ")
    if choice1 == "1":
        bob_list = [Bob['assignments'], Bob['presentation'], Bob['lab tasks'], ]
        bob_avg = sum(bob_list) / len(bob_list)
        print("Here is Bobs average score: ", bob_avg, )
        letter_grade()
        print("Would you like to check another student?: ")
        print("1.Yes")
        print("2.No")
        choice2 = input("...")
        if choice2 == "1":
            get_average()
        elif choice2 == "2":
            main()
    elif choice1 == "2":
        kaiber_list = [kaiber['assignments'], kaiber['presentation'], kaiber['lab tasks'], ]
        kaiber_avg = float(sum(kaiber_list)) / len(kaiber_list)
        print("Here is kaibers average score: ", kaiber_avg, )
        letter_grade()
        print("Would you like to check another student?: ")
        print("1.Yes")
        print("2.No")
        choice2 = input("...")
        if choice2 == "1":
            get_average()
        elif choice2 == "2":
            menu_display()


def all_student_scores():
    Bob = {'name': 'bob', 'assignments': '80', 'presentation': '80', 'lab tasks': '60'}
    kaiber = {'name': 'kaiber', 'assignments': '90', 'presentation': '90', 'lab tasks': '90'}
    all_students = [Bob['name'], kaiber['name']]
    print([all_students])
    print("Name: ", Bob['name'], "\n", "Assignments:", Bob['assignments'], "\n", "Presentation: ", Bob['presentation'],
          "\n", "Lab Tasks: ", Bob['lab tasks'])
    print("Name: ", kaiber['name'], "\n", "Assignments:", kaiber['assignments'], "\n", "Presentation: ",
          kaiber['presentation'], "\n", "Lab Tasks: ", kaiber['lab tasks'])
    menu_display()


def letter_grade():
    if bob_avg or kaiber_avg >= 90:
        print("Graded as HD")
    elif bob_avg or kaiber_avg >= 80:
        print("Graded as D")
    elif bob_avg or kaiber_avg >= 70:
        print("Graded as CR")
    elif bob_avg or kaiber_avg >= 60:
        print("Graded as P")
    elif bob_avg or kaiber_avg <= 59:
        print("Graded as F")


def menu_display():
    print("1. See all students class scores.")
    print("2. See all students average score.")
    print("3. See a specific students average score.")
    print("4. See the class average.")
    print("5.Exit")
    choice = int(input("Which would you like to see?: "))
    main(choice)


def main(choice):
    if choice == 1:
        all_student_scores()
    elif choice == 2:
        average()
    elif choice == 3:
        get_average()
    elif choice == 4:
        average()
    elif choice == 5:
        exit()
    else:
        exit()


menu_display()
