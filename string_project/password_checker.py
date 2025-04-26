MIN_LENGTH = 8
SPECIAL_CHARACTERS = ['*', '#', '$']

#We are checking for length of password, special characters,
def password_checker(password_to_check):
    list_of_characters_to_check = ['A', 'a', 'E', 'e', 'S', 's']
    list_of_counts =[0,0,0,0,0,0]
    if len(password_to_check) < MIN_LENGTH:
        return "Too short! 8 or more characters required!"
    does_it_have_a_special_character = False
    for special_character in SPECIAL_CHARACTERS:
        if special_character in password_to_check:
            does_it_have_a_special_character = True
            break;

    is_not_all_lower = False
    if password_to_check != password_to_check.lower():
        is_not_all_lower = True
    is_not_all_upper = False
    if password_to_check != password_to_check.upper():
        is_not_all_upper = True

    for index in range(len(list_of_characters_to_check)):
        character = list_of_characters_to_check[index] #['A','a','B'
        if password_to_check.find(character) == -1:
            print('not found')
        else:
            for password_character in password_to_check:
                if password_character == character:
                    list_of_counts[index] += 1
    print(list_of_counts)
    #We are going to check all of our flags to see if they are good to go (True) then return a "Password is secure"
    if (does_it_have_a_special_character and
            is_not_all_lower and
            is_not_all_upper):
        return "Secure!"
    else:
        return "Not Secure!"


def main():
    list_of_passwords = ["password", "password*", "Password*", "PASSWORD*"]
    for password in list_of_passwords:
        print(password_checker(password))

if __name__ == '__main__':
    main()