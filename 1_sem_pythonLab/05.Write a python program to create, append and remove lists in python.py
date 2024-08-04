# Create an empty list
my_list = []

# Append elements to the list
my_list.append(1)
my_list.append(2)
my_list.append(3)
print("List after appending elements:", my_list)

# Remove elements from the list
my_list.remove(2)
print("List after removing element 2:", my_list)

# extend another element to the list
x= [6,5,8]
my_list.extend(x)
print("List after extendending :", my_list)

# Remove the last element from the list
last_element = my_list.pop(3)

print ("List after extendending :" ,last_element)
