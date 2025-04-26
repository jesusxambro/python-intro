import pickle

with open('phonebook.dat', 'rb') as inputfile:
    pb = pickle.load(inputfile)

print(pb)