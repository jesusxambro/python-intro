

App: TODO List

Should:
- View
- Create
- Add
- Delete
- Search

Loop through range of {methods}.
Asking the user in a loop?


how to handle deletions within limits of txt file handling.

we can append at the end. if we use w completely erases the file. read doesn't do yet. 

1. Ingest the items as a list. [ ["ID", """title ", "location",], [items in string form] ]
2. look for the id to delete
    a. Loop through the list and check the first string in the big list.
    b. If the id inside the list is the one we want to delete, we remove it from the list.
4. write a completely new file with the 'w' mode, save the list that has removed the item to delete
5. done 