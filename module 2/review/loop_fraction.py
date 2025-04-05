#     Write a loop that calculates the total of the following series of numbers:
#
# 1/30   + 2/29   +    3/28   . . . . + 30/1

total = 0
numerator = 1
denominator = 30

while numerator <= 30:
    total = total + (numerator/denominator)
    numerator = numerator + 1
    denominator = denominator -1

