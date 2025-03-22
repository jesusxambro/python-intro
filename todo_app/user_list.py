#ask the user a list of methods
# - View
# - Create
# - Edit/Update
# - Delete
# - Search
import random

def delete_todo_item():
    print("To-Do Deletion")
    id_to_delete = int(input("What is the ID of the item to delete?"))
    list_of_items = []
    with open('todo_items.txt', 'r') as todo_items_file:
        item_id = todo_items_file.readline()
        while item_id != '':

            item_title = todo_items_file.readline()
            item_description = todo_items_file.readline()
            item_location = todo_items_file.readline()
            item_time = todo_items_file.readline()
            item_completed = todo_items_file.readline()

            item_id = item_id.strip()
            item_id = int(item_id)
            item_title = item_title.strip()
            item_description = item_description.strip()
            item_location = item_location.strip()
            item_time = item_time.strip()
            item_completed = item_completed.strip()
            item_completed = eval(item_completed)

            current_item = []
            current_item.append(item_id)
            current_item.append(item_title)
            current_item.append(item_description)
            current_item.append(item_location)
            current_item.append(item_completed)

            #add our item which is a list of strings, into the main list of the method
            list_of_items.append(current_item)

            item_id = todo_items_file.readline()
    #Assuming we have items in our list
    #TODO: How to check if the list is empty or not and handle the case

    for each_todo_list in list_of_items:
        #["ID","title","desc..."]
        if id_to_delete == each_todo_list[0]:
            #We want to delete this item in the list
            list_of_items.remove(each_todo_list)
    print("Deletion completed")


def view_todo_items():
    #TODO: Add try/except
    with open('todo_items.txt', 'r') as todo_items_file:
        item_id = todo_items_file.readline()
        while item_id != '':

            item_title = todo_items_file.readline()
            item_description = todo_items_file.readline()
            item_location = todo_items_file.readline()
            item_time = todo_items_file.readline()
            item_completed = todo_items_file.readline()

            item_id = item_id.strip()
            item_title = item_title.strip()
            item_description = item_description.strip()
            item_location = item_location.strip()
            item_time = item_time.strip()
            item_completed = item_completed.strip() #False


            print("Here are the To-Do Items: ")
            print("To-Do Id:" + item_id)
            print("To-Do Title:" + item_title)
            print("To-Do Description:" + item_description)
            print("To-Do Location:" + item_location)
            print("To-Do Time:" + item_time)
            print("To-Do Completion:" + item_completed)

            item_id = todo_items_file.readline()

def create_todo_item():
    #Think about how we want to structure a todo item.
    # time, description, title, location, completed?
    #TODO: Handle existing files
    try:
        with open('todo_items.txt', 'w') as todo_items_file:
            item_title = input("Enter the To-Do Item Title:")
            item_description = input("Enter the To-Do Item Description:")
            item_location = input("Enter the To-Do Item Location:")
            item_time = input("Enter the To-Do Item Time:")
            item_completed = False

            random_id = random.randint(0, 10000)
            todo_items_file.write(f'{random_id}\n')
            todo_items_file.write(f'{item_title}\n')
            todo_items_file.write(f'{item_description}\n')
            todo_items_file.write(f'{item_location}\n')
            todo_items_file.write(f'{item_time}\n')
            todo_items_file.write(f'{item_completed}\n')
    except Exception as err:
        print(f'There was an exception: {err}')

list_of_methods = ["1. View", "2. Create", "3. Edit", "4. Delete", "5. Search"]

for method in list_of_methods:
    print(method)

try:
    user_input = int(input("Choose which action to take from the menu")) #Example they type in 1, we should view the items
except Exception as e:
    #TODO: send the user back for input somehow
    print(f"There was an exception: {e}")

#TODO: refactor the if blocks to use elif

if user_input == 1:
    view_todo_items()
if user_input == 2:
    create_todo_item()
if user_input == 3:
    pass





if user_input == 4:
    delete_todo_item()
if user_input == 5:
    pass

# Loop through the options and display
# Then we ask the user for input on what they want to do?
# run the method they asked for
    #Maybe each methods brings us back to the original loop?
