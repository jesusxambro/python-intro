import pickle

sample_data = {
    'name': 'Jesus',
    'age': 30,
    'is_student': False,
    'courses': ['Math', 'Science']
}

with open('data.pkl', 'wb') as file:
    pickle.dump(sample_data, file)

print("Data has been pickled and saved to 'data.pkl'.")

with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print("\nUnpickled Data:")
print(loaded_data)
