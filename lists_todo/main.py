import matplotlib.pyplot as plt

def create_todo_item(incoming_todo_list):
    working_list = [todo for todo in incoming_todo_list]
    user_input_todo = input("Enter TO DO item: ")
    working_list.append(user_input_todo)
    print(f"{user_input_todo}, was added to the list.")
    return working_list

def delete_todo_item(incoming_todo_list, number_of_completed_todos):
    #TODO: add a deep copy/ copy by value to the incoming list and return the new list
    todo_to_delete = int(input("Enter TO DO item key to delete: "))
    incoming_todo_list.remove(incoming_todo_list[todo_to_delete])
    # del list_of_to_dos[todo_to_delete] :Another way to delete an item
    print(f"Item with ID: {todo_to_delete}, was deleted.")
    #add one to our accumulator and return
    updated_completion = number_of_completed_todos + 1
    return incoming_todo_list, updated_completion

def main():
    list_of_to_dos = [] #len(list) = 2
    number_of_completed_todos = 0

    def view_todo_items():
        print("Items in the list of To Do:")
        for index in range(len(list_of_to_dos)):
            print(f"\nID: {index}. {list_of_to_dos[index]}\n")

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
            list_of_to_dos = create_todo_item(list_of_to_dos)

        if user_input == 3:
            #TODO: Refactor the edit function to follow the style of create and delete functions
            edit_todo_item()

        if user_input == 4:
            list_of_to_dos, number_of_completed_todos = delete_todo_item(list_of_to_dos, number_of_completed_todos)
            create_pie_chart_of_todos(list_of_to_dos, number_of_completed_todos)

        if user_input == 5:
            search_for_todo()
        if user_input == 6:
            break


def create_pie_chart_of_todos(list_of_to_dos, number_of_completed_todos):
    list_for_pie_chart = [number_of_completed_todos, len(list_of_to_dos)]
    plt.pie(x=list_for_pie_chart, colors=("r","g"))
    plt.ylabel("Number of Completed/Remaining Todos")

    plt.show()


if __name__ == '__main__':
    main()