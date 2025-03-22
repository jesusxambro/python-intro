my_file = open("friends.txt", "a+t")
# print(my_file.read())

my_file.write("\nWonderwoman")
my_file.close()

# my_csv = open("example_csv.csv", 'r')
# for lines in my_csv:
#     print(lines)


number_to_count = 0

while number_to_count <= 9000:
    number_to_count += 1
print(number_to_count)

for num in range(4):
    print(num)