class Book():
    def __init__(self,title, author, pub_year, genre):
        self.__title = title
        self.__author = author
        self.__pub_year = pub_year
        self.__genre = genre
    def get_title(self):
        return self.__title
    def __str__(self):
        return f"Book title: {self.__title}. Author: {self.__author}"

class Catalog():
    def __init__(self):
        self.__list_of_books = []
    def add_book(self, book_to_add):
        self.__list_of_books.append(book_to_add)
    def get_all_books(self):
        return self.__list_of_books

def add_book(catalog):
    title = input("What's the title of the book? ")
    author = input("Who is the author of the book? ")
    pub_year = input("What's the publication year of the book? ")
    genre = input("What's the genre of the book? ")
    new_book_to_add = Book(title, author, pub_year, genre)
    catalog.add_book(new_book_to_add)
    print(f"{new_book_to_add.get_title()} was added to the catalog!\n")


def view_books(catalog):
    for book in catalog.get_all_books():
        print(book)


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
            view_books(catalog)
        if user_input == 2:
            add_book(catalog)
        if user_input == 6:
            break
if __name__ == '__main__':
    main()