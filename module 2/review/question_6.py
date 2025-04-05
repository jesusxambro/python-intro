# Write  a loop that sums up  of all the  numbers  that are divisible by 3 between  1 and 20.
# The final sum should be printed  when the  loop is done.  Hint:  If a number  is divisible by 3,
# the remainder  when the number  is divided by 3 is zero.
# A main function is not required – just the loop  and the variables that need to be initialized.

#need to go through 1 and 20, and check if divisible by 3
#need a variable called sum before the loop to 0

sum = 0

for number in range(1,21, 1):
    if number % 3 == 0:
        sum += number
print(f"Sum is: {sum}")