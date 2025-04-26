#lower
global_car = "HONDA"
# print(global_car.lower())
global_car = global_car.lower()
print(global_car)

global_car = "  \nhonda"
print(global_car)
global_car = global_car.lstrip()
print(global_car)

civic = "honda civic"
accord = "honda accord"
camry = "toyota camry"

honda_to_remove = "honda"
list_of_cars = [civic, accord, camry]

for index in range(len(list_of_cars)):
    car = list_of_cars[index]
    car = car.lstrip(honda_to_remove)
    car = car.lstrip()
    list_of_cars[index] = car

print(list_of_cars)