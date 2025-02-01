import random

def generate_random_number(min_val, max_val):
  return random.randint(min_val, max_val)

random_number = generate_random_number(1, 19)
print(random_number)