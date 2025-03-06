import example_math_module

def multiplication():
    print(4*4)


def main():
    print("We are in main.")
    print(example_math_module.add_two_numbers(1,2))
    print(multiplication())


# main()
if __name__ == '__main__':
    main()

