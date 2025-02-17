
count_hours = 0
count_minutes = 0

while count_hours < 10:
    while count_minutes < 5:
        count_minutes += 1

    count_hours += 1

print(f"Hour count is {count_hours} and the minute is {count_minutes}")

#start at 0
for outer_number in range(0,5,1):
    #immediately go into the inner loop
    for inner_number in range(0,3):  #0 1 2
        print("Inside the inner loop!")
    print("Inside the OUTER Loop!")

print("In the main code!")