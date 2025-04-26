numbers = [1,2,3,4]
squares = {}
for number in numbers:
    squares[number] = number ** 2
print(squares)

squares = {item:item**2 for item in numbers}
print(squares)

dict1 = {'A':1, 'B':2, 'C':3}
dict2 = {k:v for k,v in dict1.items()}
print(dict2)

spotted_species = { "cool frog": 120, "spotted deer": 300, "cougar": 3, "zebra": 1}
# largest = {k:v for k,v in populations.items() if v > 2000000}
species_over_100 = {k:v for k,v in spotted_species.items() if v > 100}
print(species_over_100)


alaskan_car = {
    "make": "subaru",
    "model": "forester",
    "color": "blue"
}

seoul_car = {
    "make": "hyundai",
    "model": "elantra",
    "color": "black"
}
my_garage = {"usa": alaskan_car, "rok":seoul_car}


my_list = [alaskan_car, seoul_car]
for car in my_list:
    print(car.get("model"))

# example_data = [('apple', 10), ('banana', 20), ('cherry', 30)]
# fruit_dict = {key: value for key, value in example_data}
# print(fruit_dict)