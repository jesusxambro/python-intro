# Write  a program  that writes  random  integers  to a file.
# The  program  should  read  in two numbers from the user: one that specifies how many random numbers to generate,
# and one that specifies the  top  of the  range  of random  numbers  (that is, 100 if the  user wants  numbers  between  1 and  100, inclusive).
# Write  the numbers  to a file called "random_numbers.txt".  Put  each number  on a new line.
import random


def variable_random_numbers(amount_of_random_numbers, max_range):
    # amount_of_random_numbers_input = input("# of numbers wanted: ")
    # max_range_input = input("Maximum of random range: ")
    open_file = open("random_numbers.txt", "w")
    #3
    for number in range(amount_of_random_numbers):
        random_number_generated = random.randrange(1, (max_range + 1))
        string_random_number = str(random_number_generated)
        open_file.write(f"{string_random_number}\n")
        #outfile.write(str(random.randrange(1,max_num+1))+"\n")
    open_file.close()
