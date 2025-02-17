
user_input = input("Enter your favorite number")


#does not work with negative numbers
while not user_input.isdigit():
    user_input = input("Enter your favorite number")

print(user_input)

# while (score := int(input('Enter your score: '))) < 0:
#        print('The score cannot be negative.')
#
# print(f"Your score is {score}!")



userInput = 0
while True:
    try:
        userInput = int(input("Enter a number: "))
        # break
    except ValueError:
        print("Not a number!")
        continue
    else:
        print("Yes a number!")
        break









