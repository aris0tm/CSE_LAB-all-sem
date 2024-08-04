# save it as fibonacci.py in C:\Python39\Lib\site-packages

def fibonacci_sequence(n):
    """Function to generate the Fibonacci sequence up to the nth term"""
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def fibonacci_number(n):
    """Function to find the nth Fibonacci number"""
    fib_sequence = fibonacci_sequence(n)
    return fib_sequence[-1]


# Then create a new file and write this code to it 
#<----! REMOVE TRIPLE COLAN (line:19 , line:34) !---->
'''
# main.py

import fibonacci

# Input the number of terms in the Fibonacci sequence
n = int(input("Enter the number of terms in the Fibonacci sequence: "))

# Generate the Fibonacci sequence up to the nth term
sequence = fibonacci.fibonacci_sequence(n)
print("Fibonacci sequence up to the", n, "th term:", sequence)

# Find the nth Fibonacci number
nth_fibonacci = fibonacci.fibonacci_number(n)
print("The", n, "th Fibonacci number is:", nth_fibonacci)

'''