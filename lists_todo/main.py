def main():
    list_of_to_dos = []
    #Adds a user inputed todo item into our list
    def create_todo_item():
        user_input_todo = input("Enter TO DO item: ")
        list_of_to_dos.append(user_input_todo)
        print(f"{user_input_todo}, was added to the list.")

    def view_todo_items():
        print("Items in the list of To Do:")
        for index in range(len(list_of_to_dos)):
            print(f"\nID: {index}. {list_of_to_dos[index]}\n")

    def delete_todo_item():
        #list ["finish app"]
        todo_to_delete = int(input("Enter TO DO item key to delete: "))
        list_of_to_dos.remove(list_of_to_dos[todo_to_delete])
        # del list_of_to_dos[todo_to_delete] :Another way to delete an item
        print(f"Item with ID: {todo_to_delete}, was deleted.")

    def edit_todo_item():
        view_todo_items()
        todo_id_to_edit = int(input("Enter TO DO item key to edit: "))
        #TODO: Look up and implement a way to edit a string to save.
        updated_todo = input(list_of_to_dos[todo_id_to_edit])
        list_of_to_dos[todo_id_to_edit] = updated_todo

    def search_for_todo():
        keyword_to_search = input("Enter a keyword to search for:\t")
        is_found = False
        for todo_item in list_of_to_dos:
            current_todo_item_list_of_words = todo_item.split()
            if keyword_to_search in current_todo_item_list_of_words:
                print(f"Yes its in the list. Index is {list_of_to_dos.index(todo_item)}\t"
                      f"To-Do: {todo_item}")
                is_found = True
                break
        if is_found:
            pass
        else:
            print("Nothing found...\n")

    def display_menu():
        list_of_methods = ["1. View", "2. Create", "3. Edit", "4. Delete", "5. Search", "6. Exit"]
        for method in list_of_methods:
            print(method)
    while True:
        display_menu()
        try:
            user_input = int(input("Choose which action to take from the menu")) #Example they type in 1, we should view the items
        except Exception as e:
            print(f"There was an exception: {e}")

        #TODO: refactor the if blocks to use elif
        if user_input == 1:
            view_todo_items()

        if user_input == 2:
            create_todo_item()

        if user_input == 3:
            edit_todo_item()

        if user_input == 4:
            delete_todo_item()

        if user_input == 5:
            search_for_todo()
        if user_input == 6:
            break
if __name__ == '__main__':
    main()