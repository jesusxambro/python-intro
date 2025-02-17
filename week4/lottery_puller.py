import random

times_asked_to_output = input("How many sets of random numbers for the lottery ?")
while not times_asked_to_output.isdigit():
    times_asked_to_output = input("How many sets of random numbers for the lottery ?")
times_asked_to_output = int(times_asked_to_output)

#4
for index in (number of times ):
    list_of_numbers = [0,0,0,0,0]
    for number in list_of_numbers:
        list_of_numbers[number] = random.random()
    print(f"This set of lottery numbers is {list_of_numbers}")

