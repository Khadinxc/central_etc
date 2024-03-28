#Created for during Certificate 4 in Cybersecurity
#Date: 13/09/21
#Version: 1.0
#Quick Times tables


lowest_number=input("Please enter the lowest number of the multiplication tables you'd like to see!:")
highest_number=input("Please enter the highest number of the multiplication tables you'd like to see!:")


for row in range(1,13):
    print('Row',f'{row:<10}', end="\t")
    print(*[str(row*col) for col in range(int(lowest_number),(int(highest_number)+1))], sep = "\t", end="\n")
