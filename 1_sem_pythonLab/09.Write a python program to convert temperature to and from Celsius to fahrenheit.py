# methord 01
def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    Formula: (Celsius * 9/5) + 32
    """
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    Formula: (Fahrenheit - 32) * 5/9
    """
    return (fahrenheit - 32) * 5/9

# Input temperature and choice from the user
temperature = float(input("Enter temperature: "))
choice = input("Enter 'C' to convert to Celsius or 'F' to convert to Fahrenheit: ")

if choice == 'C':
    # Convert to Celsius
    converted_temperature = fahrenheit_to_celsius(temperature)
    print("Temperature in Celsius:", converted_temperature)
elif choice == 'F':
    # Convert to Fahrenheit
    converted_temperature = celsius_to_fahrenheit(temperature)
    print("Temperature in Fahrenheit:", converted_temperature)
else:
    print("Invalid choice! Please enter 'C' or 'F'.")


#<<------------! if you want to use methord 02 REMOVE Triple quotes  (line:34 , line:52 ) FROM THE CODE START AND END !------------->>#

'''

# methord 02 W/o function    
# Input temperature and choice from the user
temperature = float(input("Enter temperature: "))
choice = input("Enter 'C' to convert to Celsius or 'F' to convert to Fahrenheit: ")

if choice == 'C':
    # Convert to Celsius
    converted_temperature = (temperature - 32) * 5/9
    print("Temperature in Celsius:", converted_temperature)
elif choice == 'F':
    # Convert to Fahrenheit
    converted_temperature = (temperature * 9/5) + 32
    print("Temperature in Fahrenheit:", converted_temperature)
else:
    print("Invalid choice! Please enter 'C' or 'F'.")

    '''