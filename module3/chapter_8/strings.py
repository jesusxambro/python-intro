name = "austin"

# for index in range(len(name)):
#     print(name[index + 1])

# roses = "Roses are red"
# print(roses[6])

city = "Austin"
community = "Community"
college = "College"

acc = ""
acc += city + " "
acc = acc + community + " "
acc += college
acc = "acc"


#Throws error: acc[0] = "b"
#     ~~~^^^
# TypeError: 'str' object does not support item assignment
# acc[0] = "b"

print(acc)
