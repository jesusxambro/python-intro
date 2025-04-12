basic_tuple = ("immutable","can hold values")

print(basic_tuple[0])

basic_tuple = ("string", 12, ["apple, strawberries"])

print(basic_tuple)

car_tuple = ("nissan", "jeep", "audi")
first_two_cars = car_tuple[0:2]

print(first_two_cars)

for car in car_tuple:
    print(car)

jeep_index = car_tuple.index("jeep")
print(jeep_index)

#working with mutable elements inside a tuple
basic_tuple[2].append("mango")
print(basic_tuple[2])

#converting from tuple to list:
print(basic_tuple)
list_from_tuple = list(basic_tuple)
print(list_from_tuple)