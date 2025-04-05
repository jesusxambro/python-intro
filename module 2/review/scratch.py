# Write the definition for a function switch that receives as parameters first_name and last_name and prints them in reverse order.
# Write the call to the function from main, passing two names as parameters.

def solution_one(first_name, last_name):
    print(last_name +" "+ first_name)

# One foot equals 12 inches.
# Write the definition for a function named feet_to_inches that accepts a number of feet as an argument,
# and returns the number of inches in that many feet.
def feet_to_inches(number_of_feet):
    return number_of_feet * 12

def main():
    solution_one("First", "Last")
    result = feet_to_inches(19)

main()