import numpy as np
array = np.array([1, 2, 3])
float_array = array.astype(float)
empty_array = np.empty((3,3))
full_array = np.full((3,3), 7)
list_data = [1, 2, 3]
tuple_data = (4, 5, 6)
list_array = np.array(list_data)
tuple_array = np.array(tuple_data) 
complex_array = np.array([1+2j, 3+4j, 5+6j])
real_part = np.real(complex_array)
imaginary_part = np.imag(complex_array)
print("\n",float_array)
print("\n",empty_array)
print("\n",full_array)
print("\n",list_array)
print("\n",tuple_array)
print("\n",real_part)
print("\n",imaginary_part)
