list_of_japanese_car_makers = ["toyota", "mitsubishi", "subaru"]
# 0,1,2     -1,-2,-3
#list[start : end]
favorite_car_maker = list_of_japanese_car_makers[::-1]

print(favorite_car_maker)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = numbers[1::2]
print(even_numbers)

favorite_car_maker.insert(0,"volvo")
# favorite_car_maker.extend()
print(favorite_car_maker)