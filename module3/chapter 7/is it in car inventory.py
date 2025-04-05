car_inventory = ["bmw", "subaru", "gm"]

# user_car_choice = input("Enter the name of the car maker you are looking for: ")
user_car_choice = "tesla"

if user_car_choice not in car_inventory:
    print(f"The {user_car_choice} is available in our inventory.")
else:
    print(f"Sorry, we don't have a {user_car_choice} in our inventory.")

while "volvo" not in car_inventory:
    car_inventory.append("citroen")
    if len(car_inventory) < 5:
        car_inventory.insert(-1, "volvo")
        print("in a loop")
print("out of the loop")
