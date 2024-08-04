def is_right_triangle(a, b, c):
    """Function to check if the triangle is a right-angled triangle"""
    # Sort the sides in ascending order
    sides = sorted([a, b, c])
    
    # Apply Pythagorean theorem
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    else:
        return False

# Input lengths of the sides from the user
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

# Check if the triangle is a right-angled triangle
if is_right_triangle(a, b, c):
    print("The triangle with sides {}, {}, and {} is a right-angled triangle.".format(a, b, c))
else:
    print("The triangle with sides {}, {}, and {} is not a right-angled triangle.".format(a, b, c))
