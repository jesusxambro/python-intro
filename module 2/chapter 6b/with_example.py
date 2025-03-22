import random


def write_random_numbers_to_file(filename, number_of_lines):
    with open(filename, 'w') as file:
        for _ in range(number_of_lines):
            random_number = random.randint(0, 100)
            file.write(f"{random_number}\n")

def read_random_numbers_from_file(filename):
    #TODO: Finish writing this method
    pass


if __name__ == "__main__":
    filename = "random_numbers.txt"
    number_of_lines = 10
    write_random_numbers_to_file(filename, number_of_lines)
    read_random_numbers_from_file(filename)
    print(f"Random numbers have been written to {filename}.")