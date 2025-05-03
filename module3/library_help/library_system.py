class Book():
    def __init__(self):
        pass

class Catalog():
    def __str__(self):
        pass

def add_book(catalog):
    pass

def main():
    catalog = Catalog()

    def display_menu():
        list_of_methods = ["1. View Books", "2. Add Book", "6. Exit"]
        for method in list_of_methods:
            print(method)

    while True:
        display_menu()
        try:
            user_input = int(input("Choose which action to take from the menu")) #Example they type in 1, we should view the items
        except Exception as e:
            print(f"There was an exception: {e}")

        if user_input == 1:
            pass
        if user_input == 2:
            pass
        if user_input == 6:
            break