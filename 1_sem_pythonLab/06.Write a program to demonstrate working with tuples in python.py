# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

# Accessing elements of a tuple
print("First element:", my_tuple[0])
print("Second element:", my_tuple[1])

# Slicing a tuple
print("Sliced tuple:", my_tuple[1:4])

'''# Tuple unpacking is not necessary it is advanced for biggenner
a, b, c, d, e = my_tuple
print("Unpacked values:", a, b, c, d, e)
'''
# Concatenating tuples
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
concatenated_tuple = tuple1 + tuple2
print("Concatenated tuple:", concatenated_tuple)

# Length of a tuple
print("Length of the tuple:", len(concatenated_tuple))

# Checking if an element exists in a tuple
element = 'b'
if element in concatenated_tuple:
    print(f"{element} exists in the tuple")
else:
    print(f"{element} doesn't exist in the tuple")
