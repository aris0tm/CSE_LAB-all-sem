#methord 01
# Function to find the largest of three numbers
def find_largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Input three numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Call the function and print the result
largest_number = find_largest(num1, num2, num3)
print("The largest number is:", largest_number)

#<<------------! if you want to use methord 02 REMOVE Triple quotes  (line:22 , line:39) FROM THE CODE START AND END !------------->>#

'''
#methord 02
# Input three numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Find the largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Print the result
print("The largest number is:", largest)
'''