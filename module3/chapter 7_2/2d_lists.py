matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print("Matrix:")
for row in matrix:
    print(row)

row_index = 2
column_index = 2

element = matrix[row_index][column_index]
print(f"\nElement at row {row_index }, column {column_index }: {element}")

#nested looping
print("\nIterating through the matrix:")
for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        print(f"Element at [{row}][{column}] = {matrix[row][column]}")

#list comprehension | 2 different ways
first_column = [row[0] for row in matrix]

first_element_list = []
for row in range(len(matrix)):
    first_element_list.append(matrix[row][0])

print(first_element_list)