#reverse string
def reverse_string(string):
    """Function to reverse a string"""
    return string[::-1]

# Test the function
input_string = input("Enter a string: ")
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)


# palindrome 
def is_palindrome(string):
    """Function to check if a string is palindrome"""
    return string == string[::-1]

# Test the function

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
