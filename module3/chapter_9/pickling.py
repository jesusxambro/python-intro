import pickle

phonebook = {
    "ACC" : "555-1234"
}
#Example of serialization using the pickle library:
with open('phonebook.dat', 'wb') as output_file:
    pickle.dump(obj=phonebook, file=output_file)