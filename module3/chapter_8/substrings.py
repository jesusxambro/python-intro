subaru = "Subaru"

# print(subaru.endswith("ru", -2, len(subaru)))
# print(subaru.endswith("ru"))
#
# print(subaru.startswith("Sub"))

honda = "Honda"

print(subaru.find(honda))
print(subaru.find("Su"))

acc = "Austin Community College"
list_of_found_strings = []

if acc.find("Texas") != -1:
    print("The word Texas is in the string")
    list_of_found_strings.append(acc)
else:
    print("The word Texas IS NOT in string")

dcc = acc.replace("Austin", "Dallas")
print(dcc)

austin_fc_chant = "Go Verdes! Go Verdes! Go Verdes!"
repetition_example = "Go Verdes! " * 3
modified = austin_fc_chant.replace("Verdes!", "Uzuni!")
print(modified)
print(repetition_example)