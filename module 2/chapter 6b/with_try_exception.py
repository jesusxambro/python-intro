import random

def write_random_numbers_to_file(filename, number_of_lines):
    try:
        with open(filename, 'w') as file:
            for _ in range(number_of_lines):
                random_number = random.randint(0, 100)
                file.write(f"{random_number}\n")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print(f"Random numbers have been successfully written to {filename}.")
    finally:
        print("Operation complete.")

def read_random_numbers_from_file(filename):
    #TODO: Finish this with try/except, else, and a finally
    pass

if __name__ == "__main__":
    filename = "random_numbers.txt"
    number_of_lines = 10
    write_random_numbers_to_file(filename, number_of_lines)
    read_random_numbers_from_file(filename)