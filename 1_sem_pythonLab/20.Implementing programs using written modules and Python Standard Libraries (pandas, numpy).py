# before writting the proggram check for pandas libraries 
# to install the pandas library press win + r key and type cmd after that type this command " pip install pandas numpy "
# you are all set 

import pandas as pd
import numpy as np

# Create a NumPy array
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Create a Pandas DataFrame from the NumPy array
df = pd.DataFrame(data, columns=['A', 'B', 'C'])

# Display the DataFrame
print("DataFrame created from NumPy array:")
print(df)

# Perform some operations using Pandas
print("\nOperations using Pandas:")
print("Sum of column 'A':", df['A'].sum())
print("Mean of column 'B':", df['B'].mean())
print("Max of column 'C':", df['C'].max())
