# Assume the file data.txt exists and contains several lines of text.
# Write a short program using the while loop that displays each line in the file.

text_file = open("data.txt", "r")
# line_to_display = text_file.readline()
# while line_to_display != "":
#     print(line_to_display)
#     line_to_display = text_file.readline()

for line in text_file:
    print(line)

text_file.close()