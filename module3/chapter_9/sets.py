my_garage = set(["subaru"])
print(my_garage)

my_garden = set(["tomato"])
print(my_garden)
print(len(my_garden))
my_garden.add("potato") #can throw in just the string
print(my_garden)

my_garden.update(["watermelon"]) #update expects an iterable
print(my_garden)

my_garden.remove("watermelon")
my_garden.discard("tomato") #prefer this over remove for no exception
my_garden.clear()
print(my_garden)
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)

less_than_four = {item for item in unique_numbers if item <4}
print(less_than_four)