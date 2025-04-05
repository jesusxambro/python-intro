car_inventory = ["bmw", "subaru", "gm", "gm"]

car_inventory.append("volvo")
print(car_inventory)

how_many_gm = car_inventory.count("gm")
print(f"GM is in the inventory this many times: {how_many_gm}")

if "bmw" in car_inventory:  #safer way to check if list not known or too big. Use a try block as well
    print(f"Location of BMW is : {car_inventory.index("bmw")}")

#insert
car_inventory.insert(2, "hyundai")
print(car_inventory)
#loop through list and apply lower to get all lowercase elements, then sort.

car_inventory.sort()
print(car_inventory)

#Remove
car_inventory.remove("gm")
print(car_inventory)
car_inventory.append("gm")
#a way to remove all occurrences of an element
for num_of_times in range(car_inventory.count("gm")):
    car_inventory.remove("gm")

print(car_inventory)

#Reverse
car_inventory.reverse()
print(car_inventory)


