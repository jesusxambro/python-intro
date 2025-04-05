example_list = ["finish the app", "go for a run"]

user_search = "run"

#Go through a loop of our example list
#"Finish the app"
for todo in example_list:
    #Loop through the strings, slice/split them, then ["finish","the","app"],
    # then we check if the user input is in there.If true, return with yes and ID
    current_todo_item_list_of_words = todo.split() #["finish","the","app"]
    if user_search in current_todo_item_list_of_words:
        print(f"yes its in the list. Index is {example_list.index(todo)}")
    else:
        print("not found")





