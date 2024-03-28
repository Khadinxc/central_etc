#Created for during Certificate 4 in Cybersecurity
# Date: 13/09/21
# Version: 1.0
# The user can input the amount of bricks they have and receive the height they can build to as an output
while True:
    bricks = int(input("Enter number of bricks: "))
    main = bricks+1

    for n in range(main):
        if (n * n) / 2 <= main:
            height = n
    if bricks == 0:
        height = 0

    print("The height of the pyramid is:", height)
    while True:
        answer = str(input('Run again? (y/n): '))
        if answer in ('y', 'n', 'yes',):
            break
        print("invalid input.")
    if answer == 'y' or answer == 'yes':
        continue
    else:
        print("Goodbye")
        break
