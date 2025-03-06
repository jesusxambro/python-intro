import random
import math

def get_random_radius():
    random_number_to_return = random.uniform(1, 100)
    return random_number_to_return

def get_area_of_circle(radius):
    area = (radius * radius) * math.pi
    return area


def main():
    random_radius = get_random_radius()
    area = get_area_of_circle(random_radius)
    print(f"Radius is: {random_radius}")
    print(f"Area of the circle is: {area}")


main()