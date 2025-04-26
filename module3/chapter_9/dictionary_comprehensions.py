numbers = [1,2,3,4]
squares = {}
for number in numbers:
    squares[number] = number ** 2
print(squares)

squares = {item:item**2 for item in numbers}
print(squares)



# example_data = [('apple', 10), ('banana', 20), ('cherry', 30)]
# fruit_dict = {key: value for key, value in example_data}
# print(fruit_dict)