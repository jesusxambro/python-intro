def two_numbers_to_multiply(first_number, second_number):
    return first_number * second_number



product = two_numbers_to_multiply(3,2)
print(product)


# PASS BY VALUE EXAMPLE
def subtract_two_numbers(first_number, second_number):
    first_number= first_number - second_number
    return first_number

big_number = 4
small_number = 2

new_product = subtract_two_numbers(big_number, small_number)
print(new_product)