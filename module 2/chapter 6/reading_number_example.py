reading_sales_data = open("number_example.txt", "r")

original_data = reading_sales_data.read()

converted_data = int(original_data)

print(converted_data)
print(type(converted_data))

print("\nOriginal Data:")
print(original_data)
print(type(original_data))