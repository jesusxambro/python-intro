my_garage = {"subaru": "forester"}
print(my_garage["subaru"])

my_garage["subaru"] = "impreza"

del my_garage["subaru"] #delete a key-value pair

print(my_garage)

empty_dictionary = {}

my_garage = {"subaru": "forester", "ford":"f150", "bae":"lmtv"}

for car in my_garage: #car is just a stand in for the real key, as we iterate through the dictionary
    print(my_garage[car])
my_garage.clear()

print(my_garage)
my_garage = {"subaru": "forester", "ford":"f150", "geo": "metro", "bae":"lmtv"}
print(my_garage.get("mazda"))

print(my_garage.items())
print("\n")
print(my_garage)

print(my_garage.keys())

deleted_car = my_garage.pop("bae")
print(f"Your car: {deleted_car} was deleted." )

my_garage["saab"] = "v90"

popped_car = my_garage.popitem()
print(popped_car)

print(my_garage)

print(my_garage.values())

for car in my_garage.values():
    print(car)