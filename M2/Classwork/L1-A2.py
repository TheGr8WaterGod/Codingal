# Create an empty dictionary
my_dict = {}

# Dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}  # {key: value}

# Dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

# Overwrite with a new dictionary
my_dict = {'name': 'John', 'age': 27}

# Access values
print(my_dict['name'])       # Output: John
print(my_dict.get('age'))    # Output: 27

# Update a value
my_dict['age'] = 28
print(my_dict)

# Add a new item
my_dict['address'] = 'Downtown'
print(my_dict)

# Remove a specific item
my_dict.pop('age')
print(my_dict)

# Access a specific item
print("Address:", my_dict.get('address'))

# Clear all items
my_dict.clear()
print(my_dict)  # Output: {}