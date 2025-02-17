inner_value_to_check = 0

for outer_number in range(0,5,1):
    #immediately go into the inner loop
    for inner_number in range(0,3):  #0 1 2
        if inner_value_to_check >= 3:
            break
        print("Inside the INNER loop!")
        inner_value_to_check += 1

    print("In the OUTER Loop!")

print("In the main code!")