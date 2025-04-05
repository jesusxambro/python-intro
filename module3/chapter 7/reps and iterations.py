list_of_car_makes = ["toyota", "ford", "bmw"]
new_list = list_of_car_makes * 3
print(new_list)

#iterations
for make in list_of_car_makes:
    if make == "toyota":
        print("I like tacomas")
    if make == "ford":
        print("I like mustangs")