import math


def calc_circle_is_bigger_than_square(radius, length_of_square):
    area_of_circle = (radius * radius) * math.pi
    area_of_square = length_of_square * length_of_square
    is_area_of_circle_bigger = False
    if area_of_circle > area_of_square:
        is_area_of_circle_bigger = True
    return is_area_of_circle_bigger, area_of_circle, area_of_square

def main():
    is_area_of_circle_bigger, area_of_circle, area_of_square = calc_circle_is_bigger_than_square(25,10)
    print(is_area_of_circle_bigger)
    print(area_of_circle)
    print(area_of_square)

main()