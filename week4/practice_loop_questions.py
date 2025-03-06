
task_completion = 0
user_input = input("How many times did you respond to the email since last time?")

while user_input.isdigit():

    while not user_input.isdigit():
        user_input = input("How many times did you respond to the email since last time?")

    hourly_checks = input("How many times did you check in the last hour?")

    while not hourly_checks.isdigit():
        hourly_checks = input("How many times did you check in the last hour?")

    user_input = int(user_input) #converts the string to an int
    task_completion += user_input
    check_if_user_wants_to_quit = input("Do you want to exit? Type in yes or no")
    if check_if_user_wants_to_quit == "yes":
        break
print("You didnt put in a number...")\
exit

print(f"Hey, you checked/responded {task_completion} times today...")
average_checks = task_completion / hourly_checks
print(f"On average you checked it {average_checks} times an hour...")