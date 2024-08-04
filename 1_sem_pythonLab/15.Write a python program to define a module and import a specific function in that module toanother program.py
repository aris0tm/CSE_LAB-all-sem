# save it as my_module.py in C:\Python39\Lib\site-packages
# 

def greet_user(name):
    """Function to greet the user"""
    print("Hello,", name, "!")
    
def square_number(num):
    """Function to calculate the square of a number"""
    return num ** 2
    
def find_average(numbers):
    """Function to find the average of a list of numbers"""
    return sum(numbers) / len(numbers)


# Then create a new file and write this code to it 
#<----! REMOVE TRIPLE COLAN (line:19 , line:32) !---->
'''

# main.py

from my_module import square_number

# Input a number from the user
num = float(input("Enter a number: "))

# Calculate the square of the number using the square_number function from my_module
result = square_number(num)
print("Square of", num, "is:", result)

'''