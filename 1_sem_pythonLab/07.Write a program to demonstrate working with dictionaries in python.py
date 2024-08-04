# Creating a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print("Dictionary:", my_dict)

# Accessing elements of a dictionary
print("Name:", my_dict['name'])
print("Age:", my_dict['age'])

# Modifying elements of a dictionary
my_dict['age'] = 35
print("Modified Dictionary:", my_dict)

# Adding new key-value pairs to a dictionary
my_dict['gender'] = 'Male'
print("Dictionary after adding new key-value pair:", my_dict)

# Removing elements from a dictionary
removed_value = my_dict.pop('city')
print("Removed value:", removed_value)
print("Dictionary after removing 'city':", my_dict)

# Iterating over keys and values in a dictionary
print("\nIterating over keys:")
for key in my_dict.keys():
    print(key)

print("\nIterating over values:")
for value in my_dict.values():
    print(value)

print("\nIterating over key-value pairs:")
for key, value in my_dict.items():
    print(key, ":", value)

# Checking if a key exists in a dictionary
key_to_check = 'name'
if key_to_check in my_dict:
    print(f"{key_to_check} exists in the dictionary")
else:
    print(f"{key_to_check} doesn't exist in the dictionary")
